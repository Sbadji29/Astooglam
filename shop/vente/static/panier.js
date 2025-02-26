function ajouterAuPanier(produitId) {
    fetch(`/ajouter-au-panier/${produitId}/`)
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
}

function supprimerDuPanier(produitId) {
    fetch(`/supprimer-du-panier/${produitId}/`)
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload();
    })
}      