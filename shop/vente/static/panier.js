let cartItems = [];

// Fonction pour sauvegarder le panier dans le Local Storage
function saveCart() {
    localStorage.setItem("cart", JSON.stringify(cartItems));
}

// Fonction pour récupérer le panier depuis le Local Storage
function loadCart() {
    const storedCart = localStorage.getItem("cart");
    if (storedCart) {
        cartItems = JSON.parse(storedCart);
        renderCart();
    }
}

// Fonction pour afficher les articles dans le panier
function renderCart() {
    const cartContainer = document.getElementById("cart-items");
    cartContainer.innerHTML = ""; // Vider le contenu actuel

    let totalPrice = 0;

    cartItems.forEach((item, index) => {
        totalPrice += item.prix * item.quantite;

        const cartItem = document.createElement("div");
        cartItem.classList.add("cart-item");
        cartItem.innerHTML = `
            <img src="${item.image}" alt="${item.nom}">
            <div class="item-details">
                <h3>${item.nom}</h3>
                <p class="availability">Disponible</p>
                <p class="delivery">ASTOOGLAM <span class="express">SHOP</span></p>
            </div>
            <div class="item-pricing">
                <p class="price">${item.prix} FCFA</p>
            </div>
            <div class="quantity-controls">
                <button class="quantity-btn decrease" data-index="${index}">-</button>
                <span class="quantity">${item.quantite}</span>
                <button class="quantity-btn increase" data-index="${index}">+</button>
            </div>
            <button class="delete-btn" data-index="${index}">🗑️ Supprimer</button>
        `;

        cartContainer.appendChild(cartItem);
    });

    document.getElementById("total-price").textContent = totalPrice + " FCFA";

    addCartEventListeners();
}

// Ajouter des événements pour modifier la quantité et supprimer un article
function addCartEventListeners() {
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function () {
            const index = this.getAttribute("data-index");
            cartItems.splice(index, 1);
            saveCart();
            renderCart();
        });
    });

    document.querySelectorAll(".increase").forEach(button => {
        button.addEventListener("click", function () {
            const index = this.getAttribute("data-index");
            cartItems[index].quantite += 1;
            saveCart();
            renderCart();
        });
    });

    document.querySelectorAll(".decrease").forEach(button => {
        button.addEventListener("click", function () {
            const index = this.getAttribute("data-index");
            if (cartItems[index].quantite > 1) {
                cartItems[index].quantite -= 1;
                saveCart();
                renderCart();
            }
        });
    });
}

// Charger le panier au démarrage
document.addEventListener("DOMContentLoaded", loadCart);

document.addEventListener("DOMContentLoaded", function () {
    console.log("JS chargé !");

    document.querySelectorAll(".Shopping img").forEach(img => {
        img.addEventListener("click", function (event) {
            event.preventDefault(); // Empêcher d'ouvrir une page si c'est un lien
            console.log("🛒 Produit cliqué !");
        });
    });
});
