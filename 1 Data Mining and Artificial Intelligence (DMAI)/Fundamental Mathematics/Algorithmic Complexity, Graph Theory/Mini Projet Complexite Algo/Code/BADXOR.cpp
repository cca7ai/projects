// Problème BADXOR.cpp de SPOJ résolu avec C++14

#include <iostream> // Bibliothèque standard C++, Pour les entrées/sorties
#include <vector> // Pour définir et manipuler les vecteurs
#include <unordered_set> // Pour les ensembles non ordonnés
//#include <bitset> //bibliothèque standard <bitset>, qui permet de manipuler des ensembles de bits, utilisée pour manipuler les bits et réduire la complexité et le temps d'exécution
using namespace std;

const int MODULO = 100000007;// Modulo pour les résultats

// Fonction principale
int main() {
	ios_base::sync_with_stdio(false);//désactive la synchronisation entre les flux C++ (cin, cout) et les flux C (scanf, printf). Gain de performance notable sur des grandes entrées / sorties.
    cin.tie(nullptr); //détache cin de cout car cin est lié à cout par défaut
	// Lecture du nombre de cas de test
    int test_cases;
    cin >> test_cases;
	// Vérification du nombre de cas de test
    if (test_cases < 1 || test_cases > 20) {
        cerr << "Le nombre de cas de test doit être compris entre 1 et 20.\n";
        return 1;
    }
    
    for (int case_num = 1; case_num <= test_cases; ++case_num) {
        int size_A, size_B;
        cin >> size_A >> size_B;
		// Vérification des tailles des tableaux
        if (size_A < 0 || size_B < 0) {
            cerr << "Invalid array sizes.\n";
            return 1;
        }
        // Définition et Lecture des éléments de A sous forme de vecteur
        vector<int> A(size_A);
        for (int i = 0; i < size_A; ++i) {
            cin >> A[i];
            if (A[i] < 0 || A[i] > 1000) {
                cerr << "Les éléments de A doivent être compris entre 0 et 1000.\n";
                return 1;
            }
        }
		// Définition et Lecture des éléments de B sous forme d'ensemble non ordonné
        unordered_set<int> B_set;
        for (int i = 0; i < size_B; ++i) {
            int b;
            cin >> b;
            if (b < 0 || b > 1000) {
                cerr << "Les éléments de B doivent être compris entre 0 et 1000.\n";
                return 1;
            }
			B_set.insert(b); 
        }

		vector<int> dp(1024, 0); /* Création et initialisation d'un vecteur de longueur 1024 éléments, chacun ayant la valeur initiale 0.
                                Taille fixe pour représenter tous les XOR possibles, différent avec notre programme python où on 
                                avait utilisé un dictionnaire espérant réduire la complexité et le temps d'exécution*/ 
        dp[0] = 1; // Car le sous-ensemble vide a un XOR = 0

        for (int a : A) {
			vector<int> new_dp = dp; // Copie pour mise à jour simultanée sans interférence avec anciennes valeurs
            for (int x = 0; x < 1024; ++x) {
				int new_xor = x ^ a;// Calcul du nouveau XOR
				new_dp[new_xor] += dp[x];// Ajout de la valeur actuelle au nouveau XOR
                if (new_dp[new_xor] >= MODULO) {
                    new_dp[new_xor] -= MODULO; // Réduction modulo optimisée
                }
            }
			dp = move(new_dp);// Mise à jour de dp avec new_dp
        }

        int total = 0;
        for (int x = 0; x < 1024; ++x) {
            if (!B_set.count(x)) { // Exclusion des mauvais XOR
                total = (total + dp[x]) % MODULO;
            }
        }

        cout << "Case " << case_num << ": " << total << '\n';
    }

    return 0;
}