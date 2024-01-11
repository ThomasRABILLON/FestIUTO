-- Insertion

-- INSTRUMENT
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(1, 'Guitare');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(2, 'Basse');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(3, 'Batterie');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(4, 'Piano');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(5, 'Saxophone');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(6, 'Trompette');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(7, 'Trombone');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(8, 'Violon');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(9, 'Violoncelle');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(10, 'Contrebasse');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(11, 'Harpe');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(12, 'Flûte');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(13, 'Clarinette');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(14, 'Accordéon');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(15, 'Synthétiseur');
INSERT INTO INSTRUMENT (id_instru, nom_instru) VALUES(16, 'Chant');

-- STYLE_MUSICAL
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(1, 'Rock');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(2, 'Rock n Roll');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(3, 'Hard Rock');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(4, 'Heavy Metal');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(5, 'Punk Rock');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(6, 'Pop Rock');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(7, 'Jazz');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(8, 'Swing');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(9, 'Bebop');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(10, 'Latin Jazz');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(11, 'Pop');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(12, 'Rap');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(13, 'Rap old-school');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(14, 'Rap conscient');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(15, 'Trap');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(16, 'R&B');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(17, 'Electro');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(18, 'Techno');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(19, 'House');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(20, 'Trance');
INSERT INTO STYLE_MUSICAL (id_style, libelle) VALUES(21, 'Dubstep');

-- EST_SOUS_STYLE
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(1, 2);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(1, 3);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(1, 4);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(1, 5);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(1, 6);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(7, 8);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(7, 9);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(7, 10);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(11, 6);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(12, 13);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(12, 14);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(12, 15);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(12, 16);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(17, 18);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(17, 19);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(17, 20);
INSERT INTO EST_SOUS_STYLE (id_style, id_sous_style) VALUES(17, 21);

-- GROUPE
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(1, 'groupe1', "description", 16);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(2, 'groupe2', "description", 15);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(3, 'groupe3', "description", 10);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(4, 'groupe4', "description", 3);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(5, 'groupe5', "description", 4);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(6, 'groupe6', "description", 8);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(7, 'groupe7', "description", 18);

-- ARTISTE
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(1, 'Doe', 'Joe', 1, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(2, 'Doe', 'John', 2, 15);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(3, 'Kent', 'Clark', 3, 10);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(4, 'Bezos', 'Jeff', 4, 3);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(5, 'Musk', 'Elon', 5, 4);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(6, 'Doe', 'Joe', 6, 8);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(7, 'Doe', 'John', 7, 16);

-- SPECTATEUR
-- INSERT INTO SPECTATEUR (mail, nom, prenom, date_naissance, mot_de_passe) VALUES('joe@gmail.com', 'Doe', 'Joe', date('1990-01-01', '%Y-%m-%d'), "a");
-- INSERT INTO SPECTATEUR (mail, nom, prenom, date_naissance, mot_de_passe) VALUES('john@gmail.com', 'Doe', 'John', date('1990-01-01', '%Y-%m-%d'), "a");
-- INSERT INTO SPECTATEUR (mail, nom, prenom, date_naissance, mot_de_passe) VALUES('clark@gmail.com', 'Kent', 'Clark', date('1990-01-01', '%Y-%m-%d'), "a");
-- INSERT INTO SPECTATEUR (mail, nom, prenom, date_naissance, mot_de_passe) VALUES('jeff@gmail.com', 'Bezos', 'Jeff', date('1990-01-01', '%Y-%m-%d'), "a");
-- INSERT INTO SPECTATEUR (mail, nom, prenom, date_naissance, mot_de_passe) VALUES('elon@gmail.com', 'Musk', 'Elon', date('1990-01-01', '%Y-%m-%d'), "a");

-- Admin
INSERT INTO SPECTATEUR (mail, nom, prenom, date_naissance, mot_de_passe) VALUES('admin', '', '', null, 'admin');

-- A_FAVORI
-- INSERT INTO A_FAVORI (mail, id_g) VALUES('joe@gmail.com', 1);
-- INSERT INTO A_FAVORI (mail, id_g) VALUES('joe@gmail.com', 2);
-- INSERT INTO A_FAVORI (mail, id_g) VALUES('joe@gmail.com', 3);
-- INSERT INTO A_FAVORI (mail, id_g) VALUES('john@gmail.com', 4);
-- INSERT INTO A_FAVORI (mail, id_g) VALUES('john@gmail.com', 5);
-- INSERT INTO A_FAVORI (mail, id_g) VALUES('john@gmail.com', 6);
-- INSERT INTO A_FAVORI (mail, id_g) VALUES('clark@gmail.com', 7);

-- LIEU
INSERT INTO LIEU (id_lieu, nom, emplacement) VALUES(1, 'Lieu1', 'A3');
INSERT INTO LIEU (id_lieu, nom, emplacement) VALUES(2, 'Lieu2', 'A4');
INSERT INTO LIEU (id_lieu, nom, emplacement) VALUES(3, 'Lieu3', 'A5');
INSERT INTO LIEU (id_lieu, nom, emplacement) VALUES(4, 'Lieu4', 'A6');
INSERT INTO LIEU (id_lieu, nom, emplacement) VALUES(5, 'Lieu5', 'A7');
INSERT INTO LIEU (id_lieu, nom, emplacement) VALUES(6, 'Lieu6', 'A8');
INSERT INTO LIEU (id_lieu, nom, emplacement) VALUES(7, 'Lieu7', 'A9');
INSERT INTO LIEU (id_lieu, nom, emplacement) VALUES(8, 'Lieu8', 'A10');
INSERT INTO LIEU (id_lieu, nom, emplacement) VALUES(9, 'Lieu9', 'A11');

-- TYPE_EVENEMENT
INSERT INTO TYPE_EVENEMENT (id_type_evenement, libelle) VALUES(1, 'Concert');
INSERT INTO TYPE_EVENEMENT (id_type_evenement, libelle) VALUES(2, 'Interview');
INSERT INTO TYPE_EVENEMENT (id_type_evenement, libelle) VALUES(3, 'Showcase');
INSERT INTO TYPE_EVENEMENT (id_type_evenement, libelle) VALUES(4, 'Autre');

-- EVENEMENT
INSERT INTO EVENEMENT (ref_evenement, jour_arrive, heure_arrive, jour_depart, heure_depart, duree, temps_montage, temps_demontage, est_public, a_preinscription, id_g, id_type_evenement, id_lieu) VALUES('ref1', 1, 15, 1, 16, 1, 1, 2, 1, 0, 1, 1, 1);
INSERT INTO EVENEMENT (ref_evenement, jour_arrive, heure_arrive, jour_depart, heure_depart, duree, temps_montage, temps_demontage, est_public, a_preinscription, id_g, id_type_evenement, id_lieu) VALUES('ref2', 1, 15, 1, 17, 2, 0, 0, 0, 1, 2, 2, 2);
INSERT INTO EVENEMENT (ref_evenement, jour_arrive, heure_arrive, jour_depart, heure_depart, duree, temps_montage, temps_demontage, est_public, a_preinscription, id_g, id_type_evenement, id_lieu) VALUES('ref3', 1, 22, 2, 2, 4, 2, 2, 0, 1, 3, 1, 3);
INSERT INTO EVENEMENT (ref_evenement, jour_arrive, heure_arrive, jour_depart, heure_depart, duree, temps_montage, temps_demontage, est_public, a_preinscription, id_g, id_type_evenement, id_lieu) VALUES('ref4', 2, 11, 2, 14, 3, 1, 1, 0, 0, 4, 1, 4);
INSERT INTO EVENEMENT (ref_evenement, jour_arrive, heure_arrive, jour_depart, heure_depart, duree, temps_montage, temps_demontage, est_public, a_preinscription, id_g, id_type_evenement, id_lieu) VALUES('ref5', 3, 14, 3, 15, 1, 1, 1, 1, 1, 5, 3, 5);
INSERT INTO EVENEMENT (ref_evenement, jour_arrive, heure_arrive, jour_depart, heure_depart, duree, temps_montage, temps_demontage, est_public, a_preinscription, id_g, id_type_evenement, id_lieu) VALUES('ref6', 3, 14, 3, 19, 5, 3, 2, 1, 0, 6, 1, 6);
INSERT INTO EVENEMENT (ref_evenement, jour_arrive, heure_arrive, jour_depart, heure_depart, duree, temps_montage, temps_demontage, est_public, a_preinscription, id_g, id_type_evenement, id_lieu) VALUES('ref7', 2, 17, 2, 18, 1, 1, 2, 1, 1, 7, 3, 7);

-- EST_INSCRIT
-- INSERT INTO EST_INSCRIT (mail, ref_evenement) VALUES(1, 'ref3');
-- INSERT INTO EST_INSCRIT (mail, ref_evenement) VALUES(2, 'ref5');
-- INSERT INTO EST_INSCRIT (mail, ref_evenement) VALUES(3, 'ref7');

-- TYPE_BILLET
INSERT INTO TYPE_BILLET (id_type_billet, libelle, duree, prix) VALUES(1, '1 jour', 1, 59.99);
INSERT INTO TYPE_BILLET (id_type_billet, libelle, duree, prix) VALUES(2, '2 jour', 2, 109.99);
INSERT INTO TYPE_BILLET (id_type_billet, libelle, duree, prix) VALUES(3, 'totalité festival', 3, 149.99);

-- BILLET

-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(1, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), 'joe@gmail.com', 1);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(2, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-03 14:00:00', '%Y-%m-%d %H:%i:%s'), 'john@gmail.com', 2);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(3, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), NULL, 3, 3);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(4, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), 'jeff@gmail.com', 1);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(5, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-03 14:00:00', '%Y-%m-%d %H:%i:%s'), 'elon@gmail.com', 2);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(7, date('2023-01-03 14:00:01', '%Y-%m-%d %H:%i:%s'), date('2023-01-04 14:00:00', '%Y-%m-%d %H:%i:%s'), 'john@gmail.com', 1);

-- HEBERGEMENT
INSERT INTO HEBERGEMENT (id_hebergement, nb_place_jour) VALUES(1, 20);
INSERT INTO HEBERGEMENT (id_hebergement, nb_place_jour) VALUES(2, 30);
INSERT INTO HEBERGEMENT (id_hebergement, nb_place_jour) VALUES(3, 10);
INSERT INTO HEBERGEMENT (id_hebergement, nb_place_jour) VALUES(4, 5);
INSERT INTO HEBERGEMENT (id_hebergement, nb_place_jour) VALUES(5, 2);

-- EST_HEBERGER
INSERT INTO EST_HEBERGER (id_g, id_hebergement, date_debut, date_fin, duree) VALUES(1, 1, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), 1);
INSERT INTO EST_HEBERGER (id_g, id_hebergement, date_debut, date_fin, duree) VALUES(2, 2, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-03 14:00:00', '%Y-%m-%d %H:%i:%s'), 2);
INSERT INTO EST_HEBERGER (id_g, id_hebergement, date_debut, date_fin, duree) VALUES(3, 3, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-04 14:00:00', '%Y-%m-%d %H:%i:%s'), 3);
INSERT INTO EST_HEBERGER (id_g, id_hebergement, date_debut, date_fin, duree) VALUES(4, 4, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-03 14:00:00', '%Y-%m-%d %H:%i:%s'), 2);
INSERT INTO EST_HEBERGER (id_g, id_hebergement, date_debut, date_fin, duree) VALUES(5, 5, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), 1);
INSERT INTO EST_HEBERGER (id_g, id_hebergement, date_debut, date_fin, duree) VALUES(6, 5, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), 1);

-- Insertion de données pour les triggers
-- INSERT INTO EST_HEBERGER (id_g, id_hebergement, date_debut, date_fin, duree) VALUES(7, 5, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), 1);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(10, date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-03 14:00:00', '%Y-%m-%d %H:%i:%s'), 5, 1);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(9, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), NULL, 4, 3);
-- INSERT INTO EST_INSCRIT (mail, ref_evenement) VALUES(1, 'ref1');
-- INSERT INTO EST_INSCRIT (mail, ref_evenement) VALUES(2, 'ref4');
-- INSERT INTO EST_INSCRIT (mail, ref_evenement) VALUES(2, 'ref6');