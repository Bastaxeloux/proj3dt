# Segmentation d'images cardiaques 3D+T
## Projet de la filière IMA à Télécom Paris

### Auteurs:
- **LE GUILLOUZIC Maël**
- **DE BATS Martin**

### Introduction
Le traitement d'images médicales est un domaine de recherche en pleine expansion. Dans ce contexte, la segmentation d'images cardiaques est un enjeu majeur pour les profession

Notre projet de la filière IMA à Télécom Paris, consiste à segmenter le ventricule gauche d'images cardiaques 3D+T.
Le T désigne la dimension temporelle des images, c'est à dire qu'il s'agit en quelque sorte d'une vidéo 3D.

Notre objectif est de segmenter ce ventricule gauche en utilisant uniquement des méthode "au pixel" et sans réseau de neurone.

Voici le plan de notre présentation. Le rapport complet en pdf fait office de rapport final.

### Table des matières
1. Introduction
2. Le DataSet
    - 2.1 Le Jeu de données ACDC
    - 2.2 Contenu d’un patient
3. Placement des Seeds
    - 3.1 Méthode de Hough : Théorie
        - 3.1.1 Paramètres
        - 3.1.2 Cas des cercles de rayon inconnu
        - 3.1.3 Prétraitement des Images
    - 3.2 Hough Naïf : pratique
    - 3.3 Elaboration d’un masque
    - 3.4 La motivation derrière le choix de Best Hough
    - 3.5 Best Hough
    - 3.6 Métrique d’évaluation des performances
    - 3.7 Multiple Slices
    - 3.8 Résultats du Placement des Seeds
4. Segmentation du ventricule gauche
    - 4.1 Segmentation par croissance de région
    - 4.2 Adaptation de l’algorithme à notre contexte
    - 4.3 Choix du Treshold
    - 4.4 Evaluation de la segmentation 2D
    - 4.5 Meilleures Segmentations et Pires Segmentations
5. Passage au Volume
    - 5.1 Algorithme pour obtenir la segmentation en 3D
    - 5.2 Extension des métriques à la 3D
    - 5.3 Performances 3D
    - 5.4 Observation sur un patient
6. Passage de la 3D à la 3D+t
    - 6.1 Étapes du processus
    - 6.2 Implémentation
    - 6.3 Resultats
    - 6.4 Interprétation des Résultats
    - 6.5 Problème des slices extrêmes
7. Pour aller plus loin
