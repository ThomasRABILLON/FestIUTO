CREATE DATABASE IF NOT EXISTS `festIUTO`;
use `festIUTO`;

CREATE TABLE ARTISTE (
  PRIMARY KEY (id_art),
  id_art INTEGER NOT NULL AUTO_INCREMENT,
  nom VARCHAR(50),
  prenom VARCHAR(50),
  id_g INTEGER NOT NULL,
  id_instru INTEGER NOT NULL
);

CREATE TABLE A_FAVORI (
  PRIMARY KEY (id_spec, id_g),
  id_spec INTEGER NOT NULL,
  id_g INTEGER NOT NULL
);

CREATE TABLE BILLET (
  PRIMARY KEY (id_billet),
  id_billet INTEGER NOT NULL AUTO_INCREMENT,
  debut_validite DATETIME,
  fin_validite DATETIME,
  id_spec INTEGER NOT NULL,
  id_type_billet INTEGER NOT NULL
);

CREATE TABLE EST_HEBERGER (
  PRIMARY KEY (id_g, id_hebergement),
  id_g INTEGER NOT NULL,
  id_hebergement INTEGER NOT NULL,
  date_debut DATETIME,
  date_fin DATETIME,
  duree INTEGER
);

CREATE TABLE EST_INSCRIT (
  PRIMARY KEY (id_spec, ref_evenement),
  id_spec INTEGER NOT NULL,
  ref_evenement VARCHAR(50) NOT NULL
);

CREATE TABLE EST_SOUS_STYLE (
  PRIMARY KEY (id_style, id_sous_style),
  id_style INTEGER NOT NULL,
  id_sous_style INTEGER NOT NULL
);

CREATE TABLE EVENEMENT (
  PRIMARY KEY (ref_evenement),
  ref_evenement VARCHAR(50) NOT NULL,
  date_arrive DATETIME,
  date_depart DATETIME,
  duree INTEGER CHECK (duree > 0),
  temps_montage INTEGER CHECK (temps_montage >= 0),
  temps_demontage INTEGER CHECK (temps_demontage >= 0),
  est_public BOOLEAN,
  a_preinscription BOOLEAN,
  id_g INTEGER NOT NULL,
  id_type_evenement INTEGER NOT NULL,
  id_lieu INTEGER NOT NULL
);

CREATE TABLE GROUPE (
  PRIMARY KEY (id_g),
  id_g INTEGER NOT NULL AUTO_INCREMENT,
  nom_groupe VARCHAR(50) UNIQUE,
  description VARCHAR(200),
  id_style INTEGER NOT NULL
);

CREATE TABLE HEBERGEMENT (
  PRIMARY KEY (id_hebergement),
  id_hebergement INTEGER NOT NULL AUTO_INCREMENT,
  nb_place_jour INTEGER CHECK (nb_place_jour > 0)
);

CREATE TABLE INSTRUMENT (
  PRIMARY KEY (id_instru),
  id_instru INTEGER NOT NULL AUTO_INCREMENT,
  nom_instru VARCHAR(50)
);

CREATE TABLE LIEN_RS (
  PRIMARY KEY (id_lien_rs),
  id_lien_rs INTEGER NOT NULL AUTO_INCREMENT,
  lien_rs VARCHAR(200),
  id_g INTEGER NOT NULL
);

CREATE TABLE LIEN_VIDEO (
  PRIMARY KEY (id_lien_v),
  id_lien_v INTEGER NOT NULL AUTO_INCREMENT,
  lien_video VARCHAR(200),
  id_g INTEGER NOT NULL
);

CREATE TABLE LIEU (
  PRIMARY KEY (id_lieu),
  id_lieu INTEGER NOT NULL AUTO_INCREMENT,
  nom VARCHAR(50),
  emplacement VARCHAR(50)
);

CREATE TABLE PHOTO (
  PRIMARY KEY (id_ph),
  id_ph INTEGER NOT NULL AUTO_INCREMENT,
  photo BLOB,
  id_g INTEGER NOT NULL
);

CREATE TABLE SPECTATEUR (
  PRIMARY KEY (id_spec),
  id_spec INTEGER NOT NULL AUTO_INCREMENT,
  mail VARCHAR(50),
  nom VARCHAR(40),
  prenom VARCHAR(40),
  date_naissance DATE
);

CREATE TABLE STYLE_MUSICAL (
  PRIMARY KEY (id_style),
  id_style INTEGER NOT NULL,
  libelle VARCHAR(50)
);

CREATE TABLE TYPE_BILLET (
  PRIMARY KEY (id_type_billet),
  id_type_billet INTEGER NOT NULL AUTO_INCREMENT,
  libelle VARCHAR(50),
  duree INTEGER CHECK (duree > 0)
);

CREATE TABLE TYPE_EVENEMENT (
  PRIMARY KEY (id_type_evenement),
  id_type_evenement INTEGER NOT NULL AUTO_INCREMENT,
  libelle VARCHAR(50)
);

ALTER TABLE ARTISTE ADD FOREIGN KEY (id_instru) REFERENCES INSTRUMENT (id_instru);
ALTER TABLE ARTISTE ADD FOREIGN KEY (id_g) REFERENCES GROUPE (id_g);

ALTER TABLE A_FAVORI ADD FOREIGN KEY (id_g) REFERENCES GROUPE (id_g);
ALTER TABLE A_FAVORI ADD FOREIGN KEY (id_spec) REFERENCES SPECTATEUR (id_spec);

ALTER TABLE BILLET ADD FOREIGN KEY (id_type_billet) REFERENCES TYPE_BILLET (id_type_billet);
ALTER TABLE BILLET ADD FOREIGN KEY (id_spec) REFERENCES SPECTATEUR (id_spec);

ALTER TABLE EST_HEBERGER ADD FOREIGN KEY (id_hebergement) REFERENCES HEBERGEMENT (id_hebergement);
ALTER TABLE EST_HEBERGER ADD FOREIGN KEY (id_g) REFERENCES GROUPE (id_g);

ALTER TABLE EST_INSCRIT ADD FOREIGN KEY (ref_evenement) REFERENCES EVENEMENT (ref_evenement);
ALTER TABLE EST_INSCRIT ADD FOREIGN KEY (id_spec) REFERENCES SPECTATEUR (id_spec);

ALTER TABLE EST_SOUS_STYLE ADD FOREIGN KEY (id_sous_style) REFERENCES STYLE_MUSICAL (id_style);
ALTER TABLE EST_SOUS_STYLE ADD FOREIGN KEY (id_style) REFERENCES STYLE_MUSICAL (id_style);

ALTER TABLE EVENEMENT ADD FOREIGN KEY (id_lieu) REFERENCES LIEU (id_lieu);
ALTER TABLE EVENEMENT ADD FOREIGN KEY (id_type_evenement) REFERENCES TYPE_EVENEMENT (id_type_evenement);
ALTER TABLE EVENEMENT ADD FOREIGN KEY (id_g) REFERENCES GROUPE (id_g);

ALTER TABLE GROUPE ADD FOREIGN KEY (id_style) REFERENCES STYLE_MUSICAL (id_style);

ALTER TABLE LIEN_RS ADD FOREIGN KEY (id_g) REFERENCES GROUPE (id_g);

ALTER TABLE LIEN_VIDEO ADD FOREIGN KEY (id_g) REFERENCES GROUPE (id_g);

ALTER TABLE PHOTO ADD FOREIGN KEY (id_g) REFERENCES GROUPE (id_g);


DELIMITER |

-- Trigger qui empêche d'ajouter une réservation si l'évènement n'est pas en pré-inscription
CREATE TRIGGER `reservationSiPreInscription` BEFORE INSERT ON `EST_INSCRIT` FOR EACH ROW
BEGIN
    DECLARE a_pre_inscription BOOLEAN;
    DECLARE mes VARCHAR(100);
    SELECT a_preinscription INTO a_pre_inscription FROM EVENEMENT WHERE ref_evenement = NEW.ref_evenement;
    IF NOT a_pre_inscription THEN
        SET mes = CONCAT ('Inscription impossible ', NEW.ref_evenement, ' no need reservation') ;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;
END |

-- Trigger qui empêche d'ajouter un billet si la personne a déjà un billet pour la même période
CREATE TRIGGER `pasDeuxBilletEnMemeTemps` BEFORE INSERT ON `BILLET` FOR EACH ROW
BEGIN
    DECLARE mes VARCHAR(100);
    DECLARE nb_billet INTEGER;
    SELECT COUNT(*) INTO nb_billet FROM BILLET WHERE id_spec = NEW.id_spec AND ((NEW.debut_validite BETWEEN debut_validite AND fin_validite) OR (NEW.fin_validite BETWEEN debut_validite AND fin_validite));
    IF nb_billet > 0 THEN
        SET mes = CONCAT ('Billet impossible ', NEW.id_spec, ' already have a ticket') ;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;
END |

-- Trigger qui empêche d'ajouter un évènement pour un groupe si il a deja un évènement
CREATE TRIGGER `pas2EvenementEnMemeTempsPourUnGroupe` BEFORE INSERT ON `EVENEMENT` FOR EACH ROW
BEGIN
    DECLARE mes VARCHAR(100);
    DECLARE nb_evenement INTEGER;
    SELECT COUNT(*) INTO nb_evenement FROM EVENEMENT WHERE id_g = NEW.id_g AND ((NEW.date_arrive BETWEEN date_arrive AND date_depart) OR (NEW.date_depart BETWEEN date_arrive AND date_depart));
    IF nb_evenement > 0 THEN
        SET mes = CONCAT ('Evenement impossible ', NEW.id_g, ' already have an event') ;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;
END |

-- Trigger qui empêche d'ajouter un évènement dans un lieu si il y a deja un évènement
CREATE TRIGGER `pas2EvenementSurLeMemeLieu` BEFORE INSERT ON `EVENEMENT` FOR EACH ROW
BEGIN
    DECLARE mes VARCHAR(100);
    DECLARE nb_evenement INTEGER;
    SELECT COUNT(*) INTO nb_evenement FROM EVENEMENT WHERE id_lieu = NEW.id_lieu AND ((NEW.date_arrive BETWEEN date_arrive AND date_depart) OR (NEW.date_depart BETWEEN date_arrive AND date_depart));
    IF nb_evenement > 0 THEN
        SET mes = CONCAT ('Evenement impossible ', NEW.id_lieu, ' already have an event') ;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;
END |

-- Fonction qui retourne le nombre d'artiste dans un groupe
CREATE FUNCTION `nbArtisteGroupe`(`id_groupe` INTEGER) RETURNS INTEGER
BEGIN
    DECLARE nb_artiste INTEGER;
    SELECT COUNT(*) INTO nb_artiste FROM ARTISTE WHERE id_g = id_groupe;
    RETURN nb_artiste;
END |

-- Fonction qui retourne le nombre de place restante dans un hébergement
CREATE FUNCTION `nbPlaceRestante`(`id_heber` INTEGER, `date_d` DATETIME, `date_f` DATETIME) RETURNS INTEGER
BEGIN
    DECLARE nb_place INTEGER;
    DECLARE nb_place_occupe INTEGER;
    SELECT nb_place_jour INTO nb_place FROM HEBERGEMENT WHERE id_hebergement = id_heber;
    SELECT SUM(nbArtisteGroupe(id_g)) INTO nb_place_occupe FROM EST_HEBERGER WHERE id_hebergement = id_heber AND ((date_d BETWEEN date_debut AND date_fin) OR (date_f BETWEEN date_debut AND date_fin));
    RETURN nb_place - nb_place_occupe;
END |

-- Trigger qui empeche d'ajouter un groupe dans un hébergement si il n'y a plus de place
CREATE TRIGGER `plusDePlaceHerbergement` BEFORE INSERT ON `EST_HEBERGER` FOR EACH ROW
BEGIN
    DECLARE mes VARCHAR(100);
    DECLARE nb_place_restante INTEGER;
    DECLARE nb_place_groupe INTEGER;
    SELECT nbArtisteGroupe(NEW.id_g) INTO nb_place_groupe;
    SELECT nbPlaceRestante(NEW.id_hebergement, NEW.date_debut, NEW.date_fin) INTO nb_place_restante;
    IF nb_place_restante - nb_place_groupe < 0 THEN
        SET mes = CONCAT ('Hebergement impossible ', NEW.id_hebergement, ' no more place') ;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF;
END |

-- Procédure qui affiche les hébergements disponibles pour un groupe
CREATE PROCEDURE `afficheHebergementDispo`(`id_groupe` INTEGER, `date_d` DATETIME, `date_f` DATETIME)
BEGIN
    SELECT id_hebergement FROM HEBERGEMENT WHERE nbPlaceRestante(id_hebergement, date_d, date_f) > nbArtisteGroupe(id_groupe);
END |

-- Procédure qui affiche tous les sous-style d'un style
CREATE PROCEDURE `afficheLibelleSousStyle`(`idStyle` INTEGER)
BEGIN
    SELECT libelle AS `SOUS-STYLE` FROM STYLE_MUSICAL WHERE id_style IN (SELECT id_sous_style FROM EST_SOUS_STYLE WHERE id_style = idStyle);
END |

-- Procédure qui affiche tous les groupes d'un style si le style est un style principal, sinon affiche tous les groupes d'un sous-style
CREATE PROCEDURE `afficheGroupeStyle`(`idStyle` INTEGER)
BEGIN
    IF (SELECT COUNT(*) FROM EST_SOUS_STYLE WHERE id_sous_style = idStyle) > 0 THEN
        SELECT nom_groupe AS GROUPE FROM GROUPE WHERE id_style = idStyle;
    ELSE
        SELECT nom_groupe AS GROUPE FROM GROUPE WHERE id_style IN (SELECT id_sous_style FROM EST_SOUS_STYLE WHERE id_style = idStyle);
    END IF;
END |


DELIMITER ;
