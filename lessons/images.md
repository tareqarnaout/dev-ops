---
layout: page
title:  Digital Images
nav_exclude: true
author: Ibrahim Albluwi
---

<style>
h2 {
    font-weight: 400;           /* normal weight, not bold */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #3b7dc0ff;             /* optional: different color */
}

h3 {
    font-weight: 500;           /* bold weight */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #9c0101ff;             /* optional: different color */
}

.img-soft {
    width: 75%;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);  
}

.figure-soft {
    text-align: center;
    margin: 20px 0;
}

table thead th {
    background-color: #293150; /* dark blue */
    color: white;
    text-align: left;           /* optional: align text */
}

table td {
    vertical-align: top;       /* keep row heights compact */
}
</style>


# Digital Images
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Representing Colors

In primary school, you might have mixed paints of different (primary) colors to create new colors. Computer screens do something similar, but instead of mixing paints, they mix light of different colors. The primary colors of light are **Red**, **Green**, and **Blue** (RGB). By varying the intensity of each of these colors, we can create a wide range of colors. The set of colors that can be created is called a **color space**.

Try the RGB mixer below to see how different combinations of red, green, and blue light create different colors:

<iframe src="/11102-f25/lessons/rgb-mixer.html"
        style="width: 100%; height: 360px; border: none;">
</iframe>

{: .important-title }
> **Color Models**
> 
> While RGB is the most common color model for digital displays, there are other color models used in various applications, such as CMYK (Cyan, Magenta, Yellow, Black) for printing, and HSL (Hue, Saturation, Lightness) for color selection in design software. Each color model has its own advantages and is suited for specific tasks.

### Color Depth

The intensity of each primary color (Red, Green, Blue) is represented using a certain number of bits. The most common representation uses **8 bits** (1 byte) per channel. I.e., 8 bits for Red, 8 bits for Green, and 8 bits for Blue, which makes the 
total number of bits used to represent a single color value **24 bits** (3 bytes). This is called **Color Depth**.

Using a 24-bit color representation, each color channel (Red, Green, Blue) can take on $$2^8 = 256$$ different intensity levels (from $$0$$ to $$255$$). Therefore, the total number of possible colors in the color space would be:

$$256 \times 256 \times 256 = 16,777,216 \text{ colors}$$

While 16.7 million colors may seem like a lot, the human eye can distinguish millions of colors, and some high-end displays can show even more colors using higher color depths. Here is a summary of some common color depths:

<div>
  <table>
    <thead>
      <tr>
        <th>Color Depth</th>
        <th>Bits per Channel</th>
        <th>Total Colors</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>8-bit</td>
        <td>
          R = 3 bits<br>
          G = 3 bits<br>
          B = 2 bits
        </td>
        <td>256</td>
        <td>
          Limited color palette.<br>
          Used in GIF images and some web graphics.
        </td>
      </tr>
      <tr>
        <td>16-bit</td>
        <td>
          R = 5 bits<br>
          G = 6 bits<br>
          B = 5 bits
        </td>
        <td>65,536</td>
        <td>Used in some older devices</td>
      </tr>
      <tr>
        <td>24-bit</td>
        <td>
            R = 8 bits<br>
            G = 8 bits<br>
            B = 8 bits
        </td>
        <td>16.7 million</td>
        <td>Standard for most displays</td>
      </tr>
      <tr>
        <td>30-bit</td>
        <td>
            R = 10 bits<br>
            G = 10 bits<br>
            B = 10 bits
        </td>
        <td>1.07 billion</td>
        <td>High-end displays</td>
      </tr>
      <tr>
        <td>36-bit</td>
        <td>
            R = 12 bits<br>
            G = 12 bits<br>
            B = 12 bits
        </td>
        <td>68.7 billion</td>
        <td>Professional monitors</td>
      </tr>
    </tbody>
  </table>
</div>


{: .note }
> 
> Note: The 8-bit color format uses 3 bits for Red, 3 bits for Green, and 2 bits for Blue. This means that the Red and Green channels can take values from 0 to 7, while the Blue channel can take values from 0 to 3.

To appreciate the difference between color depths and shades the eye can perceive, try the color matching challenge below. Your task is to adjust the 8-bit color sliders to match the given 24-bit color as closely as possible.

<iframe src="/11102-f25/lessons/color-matcher.html"
        style="width: 100%; height: 520px; border: none;">
</iframe>

> **Link**.
> The following page allows showing the same image in different color depths. Try it out to see how color depth affects image quality:
> [https://www.csfieldguide.org.nz/en/interactives/image-bit-comparer/](https://www.csfieldguide.org.nz/en/interactives/image-bit-comparer/)

## Representing Images

An image captured by a digital camera or displayed on a screen is only an approximation of the real-world scene. The real world contains a continuous range of colors and details, but this cannot be stored directly on a computer. Instead, what we store is a **discretized** version of the image, where the continuous scene is divided into a grid, and each cell in the grid is given a color value. Each cell in this grid is called a **pixel** (short for "picture element").

The following link is to an interactive demo, showing how images are made of pixels. The image is of low **resolution** (i.e., has a small number of pixels). Zooming into the image reveals the pixels, and zooming in further shows the individual color values of each pixel.

> **Link**.
> [https://www.csfieldguide.org.nz/en/interactives/pixel-viewer/](https://www.csfieldguide.org.nz/en/interactives/pixel-viewer/)


### Image Quality

The quality of a digital image depends on two main factors: **resolution** and **color depth**. Resolution refers to the number of pixels in the image (e.g., 1920x1080 pixels). Both, how many pixels are used to represent the image and how many colors each pixel can display, affect the overall quality of the image. The more, the better! However, higher resolution and color depth also require more storage space.


