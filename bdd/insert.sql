INSERT INTO Jury (annee) VALUES (2025);

INSERT INTO Personne (nom, prenom) VALUES
('Claudel','Philippe'),
('Laurens','Camille'),
('Chandernagor','Françoise'),
('Decoin','Didier'),
('Ben Jelloun','Tahar'),
('Assouline','Pierre'),
('Constant','Paule'),
('Schmitt','Éric-Emmanuel'),
('Bruckner','Pascal'),
('Angot','Christine');

INSERT INTO Est_membre (id_personne, id_jury, est_president) VALUES
(1, 1, TRUE),
(2, 1, FALSE),
(3, 1, FALSE),
(4, 1, FALSE),
(5, 1, FALSE),
(6, 1, FALSE),
(7, 1, FALSE),
(8, 1, FALSE),
(9, 1, FALSE),
(10, 1, FALSE);

INSERT INTO Editeur (nom) VALUES
('Gallimard'),
('P.O.L'),
('Marchialy'),
('Julliard'),
('Albin Michel'),
('Sabine Wespieser'),
('Seuil'),
('Verdier'),
('Stock'),
('Minuit'),
('Verticales'),
('L\'Olivier');

INSERT INTO Personne (nom, prenom) VALUES
('Appanah','Nathacha'),
('Carrère','Emmanuel'),
('Deneufgermain','David'),
('Diop','David'),
('Dunant','Ghislaine'),
('Gasnier','Paul'),
('Lahens','Yanick'),
('Lamarche','Caroline'),
('Laurain','Hélène'),
('Majdalani','Charif'),
('Mauvignier','Laurent'),
('de Montesquiou','Alfred'),
('Poix','Guillaume'),
('Pourchet','Maria'),
('Thomas','David');

INSERT INTO Auteur (id_personne) VALUES
(11),(12),(13),(14),(15),
(16),(17),(18),(19),(20),
(21),(22),(23),(24),(25);

INSERT INTO Selection (numero_tour, date_selection, nb_livre, id_jury)
VALUES (1, '2025-09-03', 15, 1);

INSERT INTO Livre (titre, resume, date_parution, nb_page, isbn, prix, id_editeur, id_auteur) VALUES
('La nuit au cœur', 'Un roman choral puissant autour d\'une famille en reconstruction, traversée par la mémoire, la disparition et la résilience.', '2025-08-20', 324, '9782073080028', 22.00, 1, 1),
('Kolkhoze', 'Dans une campagne russe reculée, un village affronte la chute des certitudes et la violence de l\'histoire.', '2025-08-18', 412, '9782818061985', 24.50, 2, 2),
('La maison vide', 'Roman lauréat du Prix Goncourt 2025', '2025-08-19', 350, '9782707356741', 23.00, 10, 11),
('Tressaillir', 'Un récit intimiste et puissant', '2025-08-22', 289, '9782234097155', 21.50, 4, 14),
('Un frère', 'L\'histoire bouleversante d\'une fratrie', '2025-08-16', 298, '9782823623376', 22.50, 12, 15),
('La collision', 'Un thriller psychologique où une rencontre fortuite bouleverse des destins et fait basculer la réalité.', '2025-08-17', 382, '9782073101228', 25.00, 1, 6),
('Le bel obscur', 'Une réflexion subtile sur l\'art, la disparition et l\'identité, portée par une écriture lumineuse.', '2025-08-23', 330, '9782021603439', 22.00, 7, 8),
('Où s\'adosse le ciel', 'Entre Afrique et Europe, un récit poétique qui explore le déracinement, la justice et la mémoire des peuples.', '2025-08-15', 358, '9782260057307', 23.00, 4, 7),
('L\'adieu au visage', 'Un homme tente de se reconstruire après un accident, en redéfinissant son identité et son rapport au monde.', '2025-08-21', 276, '9782381340647', 21.00, 3, 3),
('Passagères de nuit', 'Deux femmes en fuite sillonnent la nuit française, cherchant liberté, pardon et réinvention. Grand Prix de l\'Académie française 2025.', '2025-08-25', 289, '9782848055701', 21.50, 6, 9),
('Le nom des rois', 'Une saga familiale magistrale', '2025-08-14', 445, '9782234097278', 24.00, 4, 10),
('Un amour infini', 'Saga familiale contemporaine mêlée de secrets, où l\'amour devient un espace de lutte, de désir et de vérité. Sélections Prix Goncourt et Médicis.', '2025-08-22', 302, '9782226498687', 22.50, 5, 5),
('Tambora', 'Un récit poignant sur la maternité et le deuil', '2025-08-20', 267, '9782378562588', 20.00, 8, 19),
('Le crépuscule des hommes', 'Une fresque historique sur les correspondants de guerre', '2025-08-18', 398, '9782221267660', 23.50, 4, 12),
('Perpétuité', 'Un roman sur la justice et la rédemption', '2025-08-21', 312, '9782073105455', 22.00, 1, 13);

INSERT INTO Fait_partie_de (id_livre, id_selection) VALUES
(1,1),(2,1),(3,1),(4,1),(5,1),
(6,1),(7,1),(8,1),(9,1),(10,1),
(11,1),(12,1),(13,1),(14,1),(15,1);

INSERT INTO Personnage (nom, isbn_livre) VALUES
-- La nuit au cœur (9782073080028)
('Chahinez Daoud', '9782073080028'),
('Emma', '9782073080028'),
('Nathacha Appanah', '9782073080028'),

('Hélène Carrère d\'Encausse', '9782818061985'),
('Emmanuel Carrère', '9782818061985'),
('Louis Carrère d\'Encausse', '9782818061985'),

('Marie-Ernestine', '9782707356741'),
('Marguerite', '9782707356741'),

('Michelle Rivas', '9782234097155'),

('Edouard Thomas', '9782823623376'),

('Saïd', '9782073101228'),

('Edmond', '9782021603439'),

('Bilal Seck', '9782260057307'),

('David Deneufgermain', '9782381340647'),

('Elizabeth Dubreuil', '9782848055701'),
('Régina', '9782848055701'),

('Charif Majdalani', '9782234097278'),

('astrophysicien d\'origine hongroise', '9782226498687'),
('Louise', '9782226498687'),

('Une mère nous parle de ses deux filles', '9782378562588'),

('Pierre', '9782073105455'),
('Houda', '9782073105455'),
('Laurent', '9782073105455'),
('Maeva', '9782073105455'),

('Joseph Kessel', '9782221267660'),
('Elsa Triolet', '9782221267660'),
('Martha Gellhorn', '9782221267660'),
('John Dos Passos', '9782221267660');