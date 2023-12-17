// pour permettre à la fois au client et au banquier de donner un résumé de l'appel 
import java.sql.Connection
import java.sql.DriverManager
import java.sql.PreparedStatement

fun main() {
    // Remplacez ces valeurs par les informations de votre base de données
    val url = "jdbc:postgresql://localhost:5432/your_database"
    val user = "your_username"
    val password = "your_password"

    // Chaîne de caractères à envoyer à la base de données
    val dataToInsert = "Hello, Database!"

    // Établir une connexion à la base de données
    DriverManager.getConnection(url, user, password).use { connection ->
        // Requête SQL pour l'insertion
        val sql = "INSERT INTO your_table(column_name) VALUES (?)"

        // Préparer la déclaration SQL avec un espace réservé pour la chaîne de caractères
        connection.prepareStatement(sql).use { preparedStatement ->
            // Remplacer le premier espace réservé avec la chaîne de caractères
            preparedStatement.setString(1, dataToInsert)

            // Exécuter la mise à jour
            preparedStatement.executeUpdate()
        }
    }

    println("Données insérées avec succès dans la base de données.")
}
