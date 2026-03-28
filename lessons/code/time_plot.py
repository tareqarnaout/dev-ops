#!/usr/bin/env python3
"""
Runtime Predictor.
A visual tool for teaching algorithmic complexity (Big O).

Author: Gemini 3 PRO
"""

import tkinter as tk
from tkinter import ttk
import math
from typing import List, Tuple, Optional, Dict

# --- Configuration & Constants ---
APP_TITLE = "Algorithmic Runtime Predictor"
CANVAS_W, CANVAS_H = 1000, 700

# Margins (CSS-style)
MARGIN_TOP    = 100
MARGIN_BOTTOM = 60
MARGIN_LEFT   = 80
MARGIN_RIGHT  = 40

# Animation Settings
ANIM_DURATION_MS = 300
ANIM_FPS = 60
ANIM_FRAME_DELAY = 1000 // ANIM_FPS
TOTAL_FRAMES = int(ANIM_DURATION_MS / ANIM_FRAME_DELAY)
CURVE_RESOLUTION = 300  # Number of segments in the curve

# Palette (Desmos-inspired)
COLOR_BG       = "#ffffff"
COLOR_SIDEBAR  = "#f9f9f9"
COLOR_GRID     = "#e6e6e6"
COLOR_AXIS     = "#666666"
COLOR_TEXT     = "#333333"

COLOR_A        = "#2d70b3" # Muted Blue
COLOR_B        = "#d35400" # Burnt Orange (High contrast vs Blue)
COLOR_ERROR    = "#c0392b" # Red for errors

# Initial Data
SAMPLE_A = [(10000, 0.012), (20000, 0.025), (40000, 0.050), (80000, 0.100)]
SAMPLE_B = [(10000, 0.005), (20000, 0.020), (40000, 0.080), (80000, 0.320)]

# --- Math & formatting Utilities ---

def fit_power_law(data: List[Tuple[float, float]]) -> Tuple[Optional[float], Optional[float]]:
    """
    Fits y = k * x^p using least squares on log-transformed data.
    Returns (k, p) or (None, None) if fit fails.
    """
    # Filter valid data for log-log plot (must be > 0)
    valid_points = [(n, t) for n, t in data if n > 0 and t > 0]
    
    if len(valid_points) < 2:
        return None, None

    try:
        log_n = [math.log(n) for n, t in valid_points]
        log_t = [math.log(t) for n, t in valid_points]
        
        n_len = len(log_n)
        mean_ln = sum(log_n) / n_len
        mean_lt = sum(log_t) / n_len

        num = sum((ln - mean_ln) * (lt - mean_lt) for ln, lt in zip(log_n, log_t))
        den = sum((ln - mean_ln) ** 2 for ln in log_n)

        if den == 0: 
            return None, None

        p = num / den
        # ln(k) = mean(ln(t)) - p * mean(ln(n))
        k = math.exp(mean_lt - p * mean_ln)
        return k, p
    except (ValueError, OverflowError, ZeroDivisionError):
        return None, None

def predict(k: float, p: float, n: float) -> float:
    """Calculates t = k * n^p"""
    try:
        return k * (n ** p)
    except OverflowError:
        return float('inf')

def solve_n_for_t(k: float, p: float, t: float) -> float:
    """Inverse function: n = (t/k)^(1/p). Used for graph clipping."""
    try:
        if k == 0 or p == 0: return 0
        return (t / k) ** (1.0 / p)
    except (ValueError, ZeroDivisionError, OverflowError):
        return 0

def format_number(x: float) -> str:
    """Formats numbers cleanly (e.g., 0.00012 -> 1.200e-4)."""
    if x == 0: return "0"
    if abs(x) < 0.001: 
        return f"{x:.3e}"
    # Remove trailing zeros and decimal point if integer
    return f"{x:.4f}".rstrip('0').rstrip('.')

def format_axis_large_n(val: float) -> str:
    """Formats large N values with SI suffixes (k, M, B)."""
    if val == 0: return "0"
    mag = abs(val)
    if mag >= 1e9: return f"{val/1e9:.1f}B".replace(".0B", "B")
    if mag >= 1e6: return f"{val/1e6:.1f}M".replace(".0M", "M")
    if mag >= 1e3: return f"{val/1e3:.1f}k".replace(".0k", "k")
    return format_number(val)

def get_smart_time_unit(max_seconds: float) -> Tuple[float, str]:
    """Returns divisor and label for the best fit time unit."""
    if max_seconds < 60:        return 1.0, "seconds"
    elif max_seconds < 3600:    return 60.0, "minutes"
    elif max_seconds < 86400:   return 3600.0, "hours"
    elif max_seconds < 3.15e7:  return 86400.0, "days"
    elif max_seconds < 3.15e9:  return 3.154e7, "years"
    else:                       return 3.154e9, "centuries"

# --- Main Application ---

class RuntimePredictor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(f"{CANVAS_W}x{CANVAS_H}")
        self.minsize(800, 600)
        
        # Grid Configuration: Sidebar fixed width, Canvas expands
        self.columnconfigure(1, weight=1) 
        self.rowconfigure(0, weight=1)    

        # State Variables
        self.data_A: List[Tuple[float, float]] = SAMPLE_A.copy()
        self.data_B: List[Tuple[float, float]] = SAMPLE_B.copy()
        self.fit_A: Tuple[Optional[float], Optional[float]] = (None, None) 
        self.fit_B: Tuple[Optional[float], Optional[float]] = (None, None)
        self.pred_pt_A: Optional[Tuple[float, float]] = None 
        self.pred_pt_B: Optional[Tuple[float, float]] = None 
        self.error_A: bool = False # New state for error reporting
        self.error_B: bool = False # New state for error reporting
        
        # Animation State
        self.anim_task_id = None
        self.anim_frame = 0
        self.last_dims = (0, 0)
        self.mapper_cache = None # Stores coordinate mapping functions

        self._configure_styles()
        self._build_ui()
        
        # Initial Plot
        self.recalc_and_plot(animate=True)

    def _configure_styles(self):
        style = ttk.Style(self)
        style.theme_use('clam') 
        style.configure('TFrame', background=COLOR_SIDEBAR)
        
        # Clean Button
        style.configure('Action.TButton', 
                        font=("Segoe UI", 9, "bold"), 
                        background="#e0e0e0", 
                        foreground="#333", 
                        borderwidth=1, 
                        focuscolor="none")
        style.map('Action.TButton', background=[('active', '#d0d0d0'), ('pressed', '#c0c0c0')])

        # Text styles
        style.configure('Header.TLabel', font=("Segoe UI", 11, "bold"), background=COLOR_SIDEBAR, foreground="#222")
        style.configure('Label.TLabel', font=("Segoe UI", 9), background=COLOR_SIDEBAR, foreground="#555")
        style.configure('Error.TLabel', font=("Segoe UI", 9, "bold"), background=COLOR_SIDEBAR, foreground=COLOR_ERROR)

    def _build_ui(self):
        # 1. Sidebar
        sidebar = ttk.Frame(self, width=320, padding=20)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.pack_propagate(False) # Respect width

        # --- Dataset A ---
        ttk.Label(sidebar, text="Algorithm A (Blue)", style='Header.TLabel', foreground=COLOR_A).pack(anchor="w", pady=(0, 5))
        
        # New Header: N and Time
        ttk.Label(sidebar, text="N (Input Size)    Time (seconds)", font=("Menlo", 9, "bold"), background=COLOR_SIDEBAR, foreground="#666").pack(anchor="w")
        
        self.txt_A = tk.Text(sidebar, height=6, font=("Menlo", 10), 
                             relief="flat", bg="white", 
                             highlightthickness=1, highlightbackground="#ccc")
        self.txt_A.pack(fill="x", pady=(2, 5))
        self.txt_A.insert("1.0", "\n".join(f"{n:<8} {t}" for n, t in self.data_A))
        self.lbl_error_A = ttk.Label(sidebar, text="", style='Error.TLabel') # Error Label A
        self.lbl_error_A.pack(anchor="w", pady=(0, 10))

        # --- Dataset B ---
        ttk.Label(sidebar, text="Algorithm B (Orange)", style='Header.TLabel', foreground=COLOR_B).pack(anchor="w", pady=(0, 5))
        
        # New Header: N and Time
        ttk.Label(sidebar, text="N (Input Size)    Time (seconds)", font=("Menlo", 9, "bold"), background=COLOR_SIDEBAR, foreground="#666").pack(anchor="w")
        
        self.txt_B = tk.Text(sidebar, height=6, font=("Menlo", 10), 
                             relief="flat", bg="white", 
                             highlightthickness=1, highlightbackground="#ccc")
        self.txt_B.pack(fill="x", pady=(2, 5))
        self.txt_B.insert("1.0", "\n".join(f"{n:<8} {t}" for n, t in self.data_B))
        self.lbl_error_B = ttk.Label(sidebar, text="", style='Error.TLabel') # Error Label B
        self.lbl_error_B.pack(anchor="w", pady=(0, 15))


        # Plot Button
        btn_plot = ttk.Button(sidebar, text="Update & Visualize", style='Action.TButton', 
                              command=lambda: self.recalc_and_plot(animate=True))
        btn_plot.pack(fill="x", pady=(5, 20))

        ttk.Separator(sidebar, orient="horizontal").pack(fill="x", pady=(0, 20))

        # --- Prediction ---
        ttk.Label(sidebar, text="Prediction", style='Header.TLabel').pack(anchor="w", pady=(0, 5))
        ttk.Label(sidebar, text="Target Input Size (n):", style='Label.TLabel').pack(anchor="w")
        
        self.ent_predict = ttk.Entry(sidebar, font=("Segoe UI", 10))
        self.ent_predict.pack(fill="x", pady=(2, 10))
        self.ent_predict.insert(0, "120000")
        
        btn_pred = ttk.Button(sidebar, text="Predict Runtime", style='Action.TButton', command=self.on_predict)
        btn_pred.pack(fill="x", pady=(0, 15))

        # Results Display
        self.lbl_res_A = ttk.Label(sidebar, text="A: —", font=("Segoe UI", 10, "bold"), foreground=COLOR_A, background=COLOR_SIDEBAR)
        self.lbl_res_A.pack(anchor="w")
        self.lbl_res_B = ttk.Label(sidebar, text="B: —", font=("Segoe UI", 10, "bold"), foreground=COLOR_B, background=COLOR_SIDEBAR)
        self.lbl_res_B.pack(anchor="w", pady=(5,0))

        # 2. Canvas
        self.canvas = tk.Canvas(self, bg=COLOR_BG, highlightthickness=0)
        self.canvas.grid(row=0, column=1, sticky="nsew")
        self.canvas.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        # Debounce resize events
        if abs(event.width - self.last_dims[0]) > 2 or abs(event.height - self.last_dims[1]) > 2:
            self.last_dims = (event.width, event.height)
            self.recalc_and_plot(animate=False)

    def _parse_input_data(self, text_widget: tk.Text) -> Tuple[List[Tuple[float, float]], bool]:
        """Parses input data and returns (data, error_flag)"""
        raw = text_widget.get("1.0", "end").strip()
        data = []
        error = False
        
        for line in raw.splitlines():
            try:
                parts = line.split()
                if len(parts) >= 2:
                    n, t = float(parts[0]), float(parts[1])
                    if n > 0 and t > 0: 
                        data.append((n, t))
                    else:
                        # n or t must be positive
                        error = True 
            except ValueError:
                # Failed to convert to float
                error = True
                continue # Skip bad lines
        
        # Also report error if less than 2 valid points for fit
        if len(data) < 2 and raw.strip() != "":
             error = True
             
        return sorted(data), error

    def recalc_and_plot(self, animate=False):
        # 1. Parse Data
        self.data_A, self.error_A = self._parse_input_data(self.txt_A)
        self.data_B, self.error_B = self._parse_input_data(self.txt_B)
        
        # 1b. Update Error Labels
        if self.error_A:
            self.lbl_error_A.config(text="! Data format error or <2 valid points")
        else:
            self.lbl_error_A.config(text="")
            
        if self.error_B:
            self.lbl_error_B.config(text="! Data format error or <2 valid points")
        else:
            self.lbl_error_B.config(text="")
            
        # Stop if there's a fatal error
        if self.error_A or self.error_B:
            self.canvas.delete("all")
            w = self.canvas.winfo_width()
            h = self.canvas.winfo_height()
            self.canvas.create_text(w/2, h/2, text="Data must be in the form:\nN1\tTime1\nN2\tTime2\n...", fill=COLOR_ERROR, font=("Segoe UI", 16, "bold"))
            self.fit_A = (None, None)
            self.fit_B = (None, None)
            return

        # 2. Fit Models
        self.fit_A = fit_power_law(self.data_A)
        self.fit_B = fit_power_law(self.data_B)
        
        # 3. Clear Prediction state on new data load
        self.pred_pt_A = None
        self.pred_pt_B = None
        self.lbl_res_A.config(text="A: —")
        self.lbl_res_B.config(text="B: —")
        
        # 4. Draw
        self.draw_scene(animate=animate)

    def on_predict(self):
        try:
            val_n = float(self.ent_predict.get())
            if val_n <= 0: raise ValueError
            
            # Helper to process prediction
            def process_pred(fit, label_widget):
                if fit[0] is not None:
                    t = predict(fit[0], fit[1], val_n)
                    div, unit = get_smart_time_unit(t)
                    label_widget.config(text=f"A: {format_number(t/div)} {unit}" if label_widget is self.lbl_res_A else f"B: {format_number(t/div)} {unit}")
                    return (val_n, t)
                else:
                    label_widget.config(text=label_widget.cget("text").split(":")[0] + ": Fit Error")
                    return None

            self.pred_pt_A = process_pred(self.fit_A, self.lbl_res_A)
            self.pred_pt_B = process_pred(self.fit_B, self.lbl_res_B)
            
            # Redraw (Static, then pulse)
            self.draw_scene(animate=False)
            self.animate_pulse(0)
            
        except ValueError:
            self.lbl_res_A.config(text="A: Invalid n")
            self.lbl_res_B.config(text="B: Invalid n")

    def animate_pulse(self, step):
        """Draws a ripple effect around prediction points."""
        self.canvas.delete("pulse_tag")
        if step > 8: return

        r = 6 + step * 2.5
        width = 3 - (step * 0.3)
        
        if self.mapper_cache:
            to_x, to_y = self.mapper_cache
            
            for pt, color in [(self.pred_pt_A, COLOR_A), (self.pred_pt_B, COLOR_B)]:
                if pt:
                    px, py = to_x(pt[0]), to_y(pt[1])
                    # Only pulse if visible
                    if py >= MARGIN_TOP:
                        self.canvas.create_oval(px-r, py-r, px+r, py+r, outline=color, width=width, tags="pulse_tag")

        self.after(40, lambda: self.animate_pulse(step+1))

    # --- Drawing Logic ---

    def draw_scene(self, animate=False):
        # Cancel any existing animation to prevent overlap
        if self.anim_task_id:
            self.after_cancel(self.anim_task_id)
            self.anim_task_id = None

        self.canvas.delete("all")
        
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 50 or h < 50: return

        # 1. Determine Ranges
        all_n = [p[0] for p in self.data_A + self.data_B]
        all_t = [p[1] for p in self.data_A + self.data_B]
        
        # Include predictions in range
        if self.pred_pt_A: 
            all_n.append(self.pred_pt_A[0]); all_t.append(self.pred_pt_A[1])
        if self.pred_pt_B: 
            all_n.append(self.pred_pt_B[0]); all_t.append(self.pred_pt_B[1])
            
        if not all_n:
            self.canvas.create_text(w/2, h/2, text="Enter Data to Begin", fill="#ccc", font=("Segoe UI", 16))
            return

        # Add 10-15% padding to the ranges
        n_max = max(all_n) * 1.15
        t_max_seconds = max(all_t) * 1.10
        
        # 2. Coordinate Mapping
        plot_w = w - MARGIN_LEFT - MARGIN_RIGHT
        plot_h = h - MARGIN_TOP - MARGIN_BOTTOM
        
        # X: Linear map from 0..n_max to MARGIN_LEFT..w-MARGIN_RIGHT
        def to_x(n): return MARGIN_LEFT + (n / n_max) * plot_w
        # Y: Linear map from 0..t_max to h-MARGIN_BOTTOM..MARGIN_TOP
        def to_y(t): return (h - MARGIN_BOTTOM) - (t / t_max_seconds) * plot_h
        
        self.mapper_cache = (to_x, to_y)

        # 3. Draw Static Grid & Axes
        self._draw_grid_and_axes(w, h, plot_w, plot_h, n_max, t_max_seconds, to_x)
        self._draw_header_equations(w)

        # 4. Calculate Curve Points
        pts_A = self._generate_curve_points(self.fit_A, n_max, t_max_seconds)
        pts_B = self._generate_curve_points(self.fit_B, n_max, t_max_seconds)

        # 5. Render Curves (Animated or Instant)
        if animate:
            self.anim_frame = 0
            self._animate_frame_loop(pts_A, pts_B, to_x, to_y)
        else:
            self._draw_curve_instant(pts_A, COLOR_A, to_x, to_y)
            self._draw_curve_instant(pts_B, COLOR_B, to_x, to_y)
            self._draw_overlays(to_x, to_y)

    def _draw_grid_and_axes(self, w, h, plot_w, plot_h, n_max, t_max, to_x):
        div, unit_label = get_smart_time_unit(t_max)
        
        # Grid steps
        steps = 10
        
        # X-Axis Grid
        for i in range(steps + 1):
            x = MARGIN_LEFT + (i/steps) * plot_w
            self.canvas.create_line(x, MARGIN_TOP, x, h - MARGIN_BOTTOM, fill=COLOR_GRID, width=1)
            # Label
            val = (i/steps) * n_max
            self.canvas.create_text(x, h - MARGIN_BOTTOM + 15, text=format_axis_large_n(val), 
                                    fill="#999", font=("Segoe UI", 9))

        # Y-Axis Grid
        for i in range(steps + 1):
            y = (h - MARGIN_BOTTOM) - (i/steps) * plot_h
            self.canvas.create_line(MARGIN_LEFT, y, w - MARGIN_RIGHT, y, fill=COLOR_GRID, width=1)
            # Label (converted unit)
            val_sec = (i/steps) * t_max
            self.canvas.create_text(MARGIN_LEFT - 10, y, text=format_number(val_sec / div), 
                                    fill="#999", font=("Segoe UI", 9), anchor="e")

        # Solid Axes
        self.canvas.create_line(MARGIN_LEFT, h - MARGIN_BOTTOM, w - MARGIN_RIGHT, h - MARGIN_BOTTOM, fill=COLOR_AXIS, width=2)
        self.canvas.create_line(MARGIN_LEFT, h - MARGIN_BOTTOM, MARGIN_LEFT, h - MARGIN_BOTTOM, fill=COLOR_AXIS, width=2)

        # Titles
        self.canvas.create_text(w - MARGIN_RIGHT, h - MARGIN_BOTTOM + 35, text="Input Size (n)", 
                                anchor="e", fill=COLOR_TEXT, font=("Segoe UI", 10, "bold"))
        self.canvas.create_text(MARGIN_LEFT, MARGIN_TOP - 25, text=f"Time ({unit_label})", 
                                anchor="w", fill=COLOR_TEXT, font=("Segoe UI", 10, "bold"))

    def _draw_header_equations(self, w):
        font_eq = ("Menlo", 10)
        x_pos = MARGIN_LEFT
        
        if self.fit_A[0] is not None:
            k, p = self.fit_A
            txt = f"Algorithm A: T(n) ≈ {format_number(k)} * n^{format_number(p)}"
            self.canvas.create_text(x_pos, 25, text=txt, font=font_eq, fill=COLOR_A, anchor="w")
        
        if self.fit_B[0] is not None:
            k, p = self.fit_B
            txt = f"Algorithm B: T(n) ≈ {format_number(k)} * n^{format_number(p)}"
            self.canvas.create_text(x_pos, 45, text=txt, font=font_eq, fill=COLOR_B, anchor="w")

    def _generate_curve_points(self, fit, n_max, t_max):
        k, p = fit
        if k is None: return []
        
        # Clip curve if it goes vertically off-screen
        n_limit_y = solve_n_for_t(k, p, t_max)
        n_limit = min(n_max, n_limit_y)
        
        points = []
        for i in range(CURVE_RESOLUTION + 1):
            n = (i / CURVE_RESOLUTION) * n_limit
            t = predict(k, p, n)
            points.append((n, t))
        return points

    def _animate_frame_loop(self, pts_A, pts_B, to_x, to_y):
        self.canvas.delete("anim_tag")
        
        # Determine how many points to draw based on progress
        progress = self.anim_frame / TOTAL_FRAMES
        count = int(progress * CURVE_RESOLUTION)
        
        def draw_segment(pts, color):
            if not pts: return
            sub = pts[:count+1]
            if len(sub) > 1:
                mapped = [(to_x(n), to_y(t)) for n, t in sub]
                self.canvas.create_line(mapped, fill=color, width=3, smooth=True, tags="anim_tag")

        draw_segment(pts_A, COLOR_A)
        draw_segment(pts_B, COLOR_B)

        if self.anim_frame < TOTAL_FRAMES:
            self.anim_frame += 1
            self.anim_task_id = self.after(ANIM_FRAME_DELAY, lambda: self._animate_frame_loop(pts_A, pts_B, to_x, to_y))
        else:
            # Animation finished
            self._draw_overlays(to_x, to_y)

    def _draw_curve_instant(self, pts, color, to_x, to_y):
        if len(pts) > 1:
            mapped = [(to_x(n), to_y(t)) for n, t in pts]
            self.canvas.create_line(mapped, fill=color, width=3, smooth=True, tags="anim_tag")

    def _draw_overlays(self, to_x, to_y):
        """Draws data points and prediction markers (on top of curves)."""
        h = self.canvas.winfo_height()

        def draw_set(data, pred_pt, color):
            # Prediction Lines
            if pred_pt:
                px, py = to_x(pred_pt[0]), to_y(pred_pt[1])
                # Only draw if within vertical bounds
                if py >= MARGIN_TOP:
                    self.canvas.create_line(px, py, px, h - MARGIN_BOTTOM, fill="#aaa", width=1, dash=(4, 4))
                    self.canvas.create_line(px, py, MARGIN_LEFT, py, fill="#aaa", width=1, dash=(4, 4))
                    # Dot
                    self.canvas.create_oval(px-6, py-6, px+6, py+6, fill="white", outline=color, width=2)
            
            # Data Points
            for n, t in data:
                px, py = to_x(n), to_y(t)
                if py >= MARGIN_TOP: # Clipping
                    self.canvas.create_oval(px-5, py-5, px+5, py+5, fill=color, outline=color)

        draw_set(self.data_A, self.pred_pt_A, COLOR_A)
        draw_set(self.data_B, self.pred_pt_B, COLOR_B)

if __name__ == "__main__":
    app = RuntimePredictor()
    app.mainloop()