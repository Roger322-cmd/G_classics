document.addEventListener("DOMContentLoaded", function () {
    const primary = document.getElementById("id_primary_color");
    const secondary = document.getElementById("id_secondary_color");
    const glassBg = document.getElementById("id_glass_background");
    const glassBorder = document.getElementById("id_glass_border_color");

    if (!primary || !secondary || !glassBg || !glassBorder) return;

    const preview = document.createElement("div");
    preview.classList.add("theme-preview-box");
    preview.innerHTML = `
        <div class="theme-preview-title">Live Theme Preview</div>
        <p>This preview updates instantly as you change colors.</p>
        <button type="button" class="btn btn-sm btn-primary mt-2">Primary Button</button>
    `;

    const container = primary.closest(".form-row") || primary.parentElement;
    container.parentElement.appendChild(preview);

    function updatePreview() {
        preview.style.setProperty("--primary", primary.value || "#0d6efd");
        preview.style.setProperty("--secondary", secondary.value || "#6c757d");
        preview.style.setProperty("--bg", glassBg.value || "rgba(255,255,255,0.08)");
        preview.style.setProperty("--border", glassBorder.value || "rgba(255,255,255,0.25)");
    }

    [primary, secondary, glassBg, glassBorder].forEach(input => {
        input.addEventListener("input", updatePreview);
    });

    updatePreview();
});
