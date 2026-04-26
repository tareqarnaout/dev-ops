(function () {
    const counterEl = document.getElementById("online-counter");
    if (!counterEl) return;

    const namespace = "dev-ops-course-site";
    const sessionKey = "online_counter_last_ping_minute";

    const pad2 = (n) => String(n).padStart(2, "0");

    const minuteKey = () => {
        const now = new Date();
        return [
            now.getUTCFullYear(),
            pad2(now.getUTCMonth() + 1),
            pad2(now.getUTCDate()),
            pad2(now.getUTCHours()),
            pad2(now.getUTCMinutes()),
        ].join("");
    };

    const keyForCurrentMinute = () => `online-${minuteKey()}`;

    const getCounterUrl = (key) => `https://api.countapi.xyz/get/${namespace}/${key}`;
    const hitCounterUrl = (key) => `https://api.countapi.xyz/hit/${namespace}/${key}`;

    const setCount = (count) => {
        if (typeof count === "number" && Number.isFinite(count)) {
            counterEl.textContent = `Online now: ${count}`;
            return;
        }
        counterEl.textContent = "Online now: unavailable";
    };

    const refreshCount = async () => {
        const key = keyForCurrentMinute();
        try {
            const res = await fetch(getCounterUrl(key), { cache: "no-store" });
            const data = await res.json();
            setCount(data.value || 0);
        } catch (err) {
            setCount(undefined);
        }
    };

    const pingIfNeeded = async () => {
        const key = keyForCurrentMinute();
        const lastPingMinute = sessionStorage.getItem(sessionKey);
        if (lastPingMinute === key) return;

        try {
            await fetch(hitCounterUrl(key), { cache: "no-store" });
            sessionStorage.setItem(sessionKey, key);
        } catch (err) {
            // Ignore transient network errors; the next interval will retry.
        }
    };

    const run = async () => {
        await pingIfNeeded();
        await refreshCount();
    };

    run();
    setInterval(run, 20000);
})();
