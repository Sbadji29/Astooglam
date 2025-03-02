function toggleSelection(id) {
    let element = document.getElementById(id);
    if (element) {
        element.classList.toggle("selected");
        console.log("✅ Sélection de :", id);
    } else {
        console.error("❌ Élément introuvable :", id);
    }
}
