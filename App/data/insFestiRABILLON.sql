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
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(8, 'groupe8', "description", 19);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(9, 'groupe9', "description", 20);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(10, 'groupe10', "description", 21);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(11, 'groupe11', "description", 1);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(12, 'groupe12', "description", 2);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(13, 'groupe13', "description", 5);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(14, 'groupe14', "description", 6);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(15, 'groupe15', "description", 7);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(16, 'groupe16', "description", 9);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(17, 'groupe17', "description", 11);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(18, 'groupe18', "description", 12);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(19, 'groupe19', "description", 13);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(20, 'groupe20', "description", 14);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(21, 'groupe21', "description", 17);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(22, 'groupe22', "description", 20);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(23, 'groupe23', "description", 5);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(24, 'groupe24', "description", 6);
INSERT INTO GROUPE (id_g, nom_groupe, description, id_style) VALUES(25, 'groupe25', "description", 17);


-- ARTISTE
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(1, 'Doe', 'Joe', 1, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(2, 'Doe', 'John', 2, 15);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(3, 'Kent', 'Clark', 3, 10);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(4, 'Bezos', 'Jeff', 4, 3);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(5, 'Musk', 'Elon', 5, 4);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(6, 'Doe', 'Joe', 6, 8);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(7, 'Doe', 'John', 7, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(8, 'Kent', 'Clark', 8, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(9, 'Bezos', 'Jeff', 9, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(10, 'Musk', 'Elon', 10, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(11, 'Doe', 'Joe', 11, 1);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(12, 'Doe', 'John', 12, 2);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(13, 'Kent', 'Clark', 13, 5);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(14, 'Bezos', 'Jeff', 14, 6);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(15, 'Musk', 'Elon', 15, 7);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(16, 'Doe', 'Joe', 16, 9);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(17, 'Doe', 'John', 17, 11);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(18, 'Kent', 'Clark', 18, 12);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(19, 'Bezos', 'Jeff', 19, 13);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(20, 'Musk', 'Elon', 20, 14);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(21, 'Doe', 'Joe', 21, 17);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(22, 'Doe', 'John', 22, 20);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(23, 'Kent', 'Clark', 23, 5);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(24, 'Bezos', 'Jeff', 24, 6);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(25, 'Musk', 'Elon', 25, 17);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(26, 'Doe', 'John', 1, 15);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(27, 'Kent', 'Clark', 2, 10);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(28, 'Bezos', 'Jeff', 3, 3);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(29, 'Musk', 'Elon', 4, 4);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(30, 'Doe', 'Joe', 5, 8);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(31, 'Doe', 'John', 6, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(32, 'Kent', 'Clark', 7, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(33, 'Bezos', 'Jeff', 8, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(34, 'Musk', 'Elon', 9, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(35, 'Doe', 'Joe', 10, 16);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(36, 'Doe', 'John', 11, 1);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(37, 'Kent', 'Clark', 12, 2);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(38, 'Bezos', 'Jeff', 13, 5);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(39, 'Musk', 'Elon', 14, 6);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(40, 'Doe', 'Joe', 15, 7);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(41, 'Doe', 'John', 16, 9);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(42, 'Kent', 'Clark', 17, 11);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(43, 'Bezos', 'Jeff', 18, 12);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(44, 'Musk', 'Elon', 19, 13);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(45, 'Doe', 'Joe', 20, 14);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(46, 'Doe', 'John', 21, 17);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(47, 'Kent', 'Clark', 22, 20);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(48, 'Bezos', 'Jeff', 23, 5);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(49, 'Musk', 'Elon', 24, 6);
INSERT INTO ARTISTE (id_art, nom, prenom, id_g, id_instru) VALUES(50, 'Doe', 'Joe', 25, 17);


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
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref1', 1, time('15:00:00'), 1, time('16:00:00'), time('01:00:00'), time('01:00:00'), time('02:00:00'), true, false, 200, 1, 1, 1);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref2', 1, time('15:00:00'), 1, time('17:00:00'), time('02:00:00'), time('00:00:00'), time('00:00:00'), false, true, 200, 2, 2, 2);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref3', 1, time('22:00:00'), 2, time('02:00:00'), time('04:00:00'), time('02:00:00'), time('02:00:00'), false, true, 200, 3, 1, 3);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref4', 2, time('11:00:00'), 2, time('14:00:00'), time('03:00:00'), time('01:00:00'), time('01:00:00'), false, false, 200, 4, 1, 4);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref5', 3, time('14:00:00'), 3, time('15:00:00'), time('01:00:00'), time('01:00:00'), time('01:00:00'), true, true, 200, 5, 3, 5);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref6', 3, time('14:00:00'), 3, time('19:00:00'), time('05:00:00'), time('03:00:00'), time('02:00:00'), true, false, 200, 6, 1, 6);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref7', 2, time('17:00:00'), 2, time('18:00:00'), time('01:00:00'), time('01:00:00'), time('02:00:00'), true, true, 200, 7, 3, 7);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref8', 2, time('23:00:00'), 3, time('01:00:00'), time('02:00:00'), time('01:00:00'), time('02:00:00'), true, true, 200, 8, 1, 8);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref9', 3, time('14:00:00'), 3, time('15:00:00'), time('01:00:00'), time('01:00:00'), time('01:00:00'), true, true, 200, 9, 3, 9);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref10', 3, time('14:00:00'), 3, time('19:00:00'), time('05:00:00'), time('03:00:00'), time('02:00:00'), true, false, 200, 10, 1, 1);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref11', 2, time('17:00:00'), 2, time('18:00:00'), time('01:00:00'), time('01:00:00'), time('02:00:00'), true, true, 200, 11, 3, 2);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref12', 2, time('23:00:00'), 3, time('01:00:00'), time('02:00:00'), time('01:00:00'), time('02:00:00'), true, true, 200, 12, 1, 3);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref13', 3, time('14:00:00'), 3, time('15:00:00'), time('01:00:00'), time('01:00:00'), time('01:00:00'), true, true, 200, 13, 3, 4);
INSERT INTO EVENEMENT (ref_evenement, jour_deb, heure_deb, jour_fin, heure_fin, duree, temps_montage, temps_demontage, est_public, a_preinscription, nb_place, id_g, id_type_evenement, id_lieu) VALUES('ref14', 3, time('14:00:00'), 3, time('19:00:00'), time('05:00:00'), time('03:00:00'), time('02:00:00'), true, false, 200, 14, 1, 2);

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
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(2, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), 3, 'john@gmail.com', 2);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(3, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), NULL, 3, 3);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(4, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), 'jeff@gmail.com', 1);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(5, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), 3, 'elon@gmail.com', 2);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(7, date('2023-01-03 14:00:01', '%Y-%m-%d %H:%i:%s'), date('2023-01-04 14:00:00', '%Y-%m-%d %H:%i:%s'), 'john@gmail.com', 1);

-- HEBERGEMENT
INSERT INTO HEBERGEMENT (id_hebergement, nom_hebergement, nb_place_jour) VALUES(1, 'Hotel rouge', 20);
INSERT INTO HEBERGEMENT (id_hebergement, nom_hebergement, nb_place_jour) VALUES(2, 'Hotel bleu', 30);
INSERT INTO HEBERGEMENT (id_hebergement, nom_hebergement, nb_place_jour) VALUES(3, 'Hotel azur', 10);
INSERT INTO HEBERGEMENT (id_hebergement, nom_hebergement, nb_place_jour) VALUES(4, 'Hotel or', 5);
INSERT INTO HEBERGEMENT (id_hebergement, nom_hebergement, nb_place_jour) VALUES(5, 'Gite de platine', 2);
INSERT INTO HEBERGEMENT (id_hebergement, nom_hebergement, nb_place_jour) VALUES(6, 'Gite de diamant', 10);

-- EST_HEBERGER
INSERT INTO EST_HEBERGER (id, id_g, id_hebergement, date_debut, date_fin) VALUES(1, 1, 1, 1, 2);
INSERT INTO EST_HEBERGER (id, id_g, id_hebergement, date_debut, date_fin) VALUES(2, 2, 2, 1, 3);
INSERT INTO EST_HEBERGER (id, id_g, id_hebergement, date_debut, date_fin) VALUES(3, 3, 3, 1, 3);
INSERT INTO EST_HEBERGER (id, id_g, id_hebergement, date_debut, date_fin) VALUES(4, 4, 4, 1, 3);
INSERT INTO EST_HEBERGER (id, id_g, id_hebergement, date_debut, date_fin) VALUES(5, 5, 5, 1, 2);
INSERT INTO EST_HEBERGER (id, id_g, id_hebergement, date_debut, date_fin) VALUES(6, 6, 5, 1, 2);
INSERT INTO EST_HEBERGER (id, id_g, id_hebergement, date_debut, date_fin) VALUES(7, 7, 6, 1, 2);

-- Insertion de données pour les triggers
-- INSERT INTO EST_HEBERGER (id_g, id_hebergement, date_debut, date_fin, duree) VALUES(7, 5, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), 1);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(10, date('2023-01-02 14:00:00', '%Y-%m-%d %H:%i:%s'), 3, 5, 1);
-- INSERT INTO BILLET (id_billet, debut_validite, fin_validite, mail, id_type_billet) VALUES(9, date('2023-01-01 14:00:00', '%Y-%m-%d %H:%i:%s'), NULL, 4, 3);
-- INSERT INTO EST_INSCRIT (mail, ref_evenement) VALUES(1, 'ref1');
-- INSERT INTO EST_INSCRIT (mail, ref_evenement) VALUES(2, 'ref4');
-- INSERT INTO EST_INSCRIT (mail, ref_evenement) VALUES(2, 'ref6');