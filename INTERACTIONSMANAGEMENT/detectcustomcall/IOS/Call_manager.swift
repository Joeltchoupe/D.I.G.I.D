import CallKit
import PostgresClientKit

class CallManager: NSObject, CXCallObserverDelegate {
    static let shared = CallManager()
    private let callObserver = CXCallObserver()

    override init() {
        super.init()
        callObserver.setDelegate(self, queue: nil)
    }

    func callObserver(_ callObserver: CXCallObserver, callChanged call: CXCall) {
        if call.hasEnded {
            // L'appel a été terminé
        } else if call.isOutgoing {
            // L'appel est sortant
        } else {
            // L'appel est entrant
            if let incomingNumber = call.uuid.stringValue {
                if isClientNumber(incomingNumber) {
                    // Le numéro est dans la base de données "clients"
                    handleIncomingCall()
                }
            }
        }
    }

    private func isClientNumber(_ number: String) -> Bool {
        guard let connection = makeDatabaseConnection() else {
            return false
        }

        do {
            let result = try connection.execute(
                "SELECT COUNT(*) FROM clients WHERE phone_number = $1",
                parameterValues: [number]
            )

            return result.first?.int ?? 0 > 0
        } catch {
            print("Database error: \(error)")
            return false
        }
    }

    private func makeDatabaseConnection() -> PostgresClientKit.Connection? {
        guard let connection = PostgresClientKit.Connection(
            configuration: ConnectionConfiguration(
                host: "your-database-host",
                port: 5432,
                user: "your-username",
                database: "your-database",
                password: "your-password"
            )
        ) else {
            return nil
        }

        do {
            try connection.open()
            return connection
        } catch {
            print("Database connection error: \(error)")
            return nil
        }
    }

    private func handleIncomingCall() {
        // Traitez l'appel entrant et enregistrez la durée dans un fichier
        let callDuration = // obtenir la durée de l'appel
        saveCallDuration(callDuration)
    }

    private func saveCallDuration(_ duration: String) {
        // Implémentez la logique pour enregistrer la durée de l'appel dans un fichier
        // Utilisez FileManager pour créer et écrire dans le fichier
    }
              }
      
