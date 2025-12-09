CREATE TABLE Personne (
    id_personne INT AUTO_INCREMENT,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    PRIMARY KEY(id_personne)
);

CREATE TABLE Auteur (
    id_auteur INT AUTO_INCREMENT,
    id_personne INT NOT NULL,
    biographie TEXT,
    PRIMARY KEY(id_auteur),
    UNIQUE(id_personne),
    FOREIGN KEY(id_personne) REFERENCES Personne(id_personne)
);

CREATE TABLE Jury (
    id_jury INT AUTO_INCREMENT,
    annee YEAR,
    PRIMARY KEY(id_jury)
);

CREATE TABLE Selection (
    id_selection INT AUTO_INCREMENT,
    numero_tour TINYINT,
    date_selection DATE,
    nb_livre TINYINT,
    id_jury INT NOT NULL,
    PRIMARY KEY(id_selection),
    FOREIGN KEY(id_jury) REFERENCES Jury(id_jury)
);

CREATE TABLE Editeur (
    id_editeur INT AUTO_INCREMENT,
    nom VARCHAR(100),
    PRIMARY KEY(id_editeur)
);

CREATE TABLE Livre (
    id_livre INT AUTO_INCREMENT,
    titre VARCHAR(255),
    resume TEXT,
    date_parution DATE,
    nb_page SMALLINT,
    isbn VARCHAR(30),
    prix DECIMAL(7,2),
    id_editeur INT NOT NULL,
    id_auteur INT NOT NULL,
    PRIMARY KEY(id_livre),
    UNIQUE(isbn),
    FOREIGN KEY(id_editeur) REFERENCES Editeur(id_editeur),
    FOREIGN KEY(id_auteur) REFERENCES Auteur(id_auteur)
);

CREATE TABLE Personnage (
    id_personnage INT AUTO_INCREMENT,
    nom VARCHAR(100),
    isbn_livre VARCHAR(30) NOT NULL,
    PRIMARY KEY(id_personnage),
    FOREIGN KEY(isbn_livre) REFERENCES Livre(isbn)
);

CREATE TABLE Vote (
    id_vote INT AUTO_INCREMENT,
    date_vote DATE,
    nb_voix INT DEFAULT 0,
    id_selection INT NOT NULL,
    id_livre INT NOT NULL,
    PRIMARY KEY(id_vote),
    FOREIGN KEY(id_selection) REFERENCES Selection(id_selection),
    FOREIGN KEY(id_livre) REFERENCES Livre(id_livre)
);

CREATE TABLE Est_membre (
    id_personne INT,
    id_jury INT,
    est_president BOOLEAN DEFAULT FALSE,
    PRIMARY KEY(id_personne, id_jury),
    FOREIGN KEY(id_personne) REFERENCES Personne(id_personne),
    FOREIGN KEY(id_jury) REFERENCES Jury(id_jury)
);

CREATE TABLE Fait_partie_de (
    id_livre INT,
    id_selection INT,
    PRIMARY KEY(id_livre, id_selection),
    FOREIGN KEY(id_livre) REFERENCES Livre(id_livre),
    FOREIGN KEY(id_selection) REFERENCES Selection(id_selection)
);