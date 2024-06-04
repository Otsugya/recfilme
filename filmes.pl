% Base de dados de filmes
filme('The Shawshank Redemption', drama, prisao).
filme('The Godfather', drama, mafia).
filme('Schindler\'s List', drama, guerra).
filme('The Pursuit of Happyness', drama, vida_real).
filme('Forrest Gump', drama, vida_real).

filme('The Dark Knight', acao, super_heroi).
filme('Inception', acao, mente).
filme('Die Hard', acao, policial).
filme('Terminator 2: Judgment Day', acao, ficcao_cientifica).
filme('Gladiator', acao, epico).

filme('Pulp Fiction', crime, gangster).
filme('Goodfellas', crime, mafia).
filme('Se7en', crime, serial_killer).
filme('The Departed', crime, policial).
filme('Heat', crime, assalto).

filme('The Lord of the Rings', fantasia, aventura).
filme('Harry Potter and the Philosopher\'s Stone', fantasia, magia).
filme('The Chronicles of Narnia: The Lion, the Witch and the Wardrobe', fantasia, magia).
filme('Pan\'s Labyrinth', fantasia, guerra).
filme('Avatar', fantasia, ficcao_cientifica).

% Regras para recomendação
recomenda(Genero, Subcategoria, Filme) :-
    filme(Filme, Genero, Subcategoria).
