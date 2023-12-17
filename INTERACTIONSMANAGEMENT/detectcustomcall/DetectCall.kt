import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.Bundle
import android.telephony.PhoneStateListener
import android.telephony.TelephonyManager
import android.webkit.WebView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var webView: WebView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        webView = findViewById(R.id.webView)
        webView.settings.javaScriptEnabled = true
        webView.loadUrl("file:///android_asset/index.html")

        // Enregistrez le BroadcastReceiver pour détecter les appels entrants
        val intentFilter = IntentFilter()
        intentFilter.addAction("android.intent.action.PHONE_STATE")
        registerReceiver(CallReceiver(), intentFilter)
    }

    inner class CallReceiver : BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            if (intent?.action == "android.intent.action.PHONE_STATE") {
                val state = intent.getStringExtra(TelephonyManager.EXTRA_STATE)

                if (state == TelephonyManager.EXTRA_STATE_RINGING) {
                    val incomingNumber = intent.getStringExtra(TelephonyManager.EXTRA_INCOMING_NUMBER)
                    // Appel de la fonction JavaScript dans WebView avec le numéro entrant
                    webView.evaluateJavascript("onCallReceived('$incomingNumber');", null)
                }
            }
        }
    }
}
//-------------------
import org.jetbrains.exposed.dao.IntIdTable
import org.jetbrains.exposed.sql.*
import org.jetbrains.exposed.sql.transactions.transaction

class MainActivity : AppCompatActivity() {

    // ... (le reste du code)

    inner class CallReceiver : BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            if (intent?.action == "android.intent.action.PHONE_STATE") {
                val state = intent.getStringExtra(TelephonyManager.EXTRA_STATE)

                if (state == TelephonyManager.EXTRA_STATE_RINGING) {
                    val incomingNumber = intent.getStringExtra(TelephonyManager.EXTRA_INCOMING_NUMBER)

                    // Vérifier si le numéro est dans la base de données clientsphone
                    if (isClientNumber(incomingNumber)) {
                        // Appel de la fonction JavaScript dans WebView avec le numéro entrant
                        webView.evaluateJavascript("onCallReceived('$incomingNumber');", null)
                    }
                }
            }
        }
    }

    private fun isClientNumber(number: String?): Boolean {
        return transaction {
            // Remplacez "jdbc:postgresql://your-database-url" par l'URL de votre base de données PostgreSQL
            Database.connect("jdbc:postgresql://your-database-url", driver = "org.postgresql.Driver", user = "your-username", password = "your-password")

            // Remplacez "clientsphone" par le nom de votre table clientsphone
            SchemaUtils.create(ClientPhones)
            
            val result = ClientPhones.select { ClientPhones.phoneNumber eq number }.count()
            
            result > 0
        }
    }
}

// Définissez la table clientsphone
object ClientPhones : IntIdTable() {
    val phoneNumber = varchar("phone_number", 20).uniqueIndex()
}
