import os
import telebot
import threading
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- RENDER HEALTH CHECK SERVER ---
app_flask = Flask(__name__)

@app_flask.route('/')
def health_check():
    return "Bot is Live!", 200

def run_flask():
    # Render automatically provides a PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app_flask.run(host='0.0.0.0', port=port)

# --- 🔒 CONFIG ---
TOKEN = os.getenv("BOT_TOKEN")
# Admin ID ko environment variable se lenge, default 0 agar na mile
ADMIN_ID_STR = os.getenv("ADMIN_ID", "0")
ADMIN_ID = int(ADMIN_ID_STR)

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

USERS_FILE = "users.txt"
BANNED_FILE = "banned.txt"

# --- 📂 LOAD DATA ---
def load_data(file):
    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                return set(map(int, f.read().split()))
        except:
            return set()
    return set()

def save_data(file, user_id):
    with open(file, "a") as f:
        f.write(f"{user_id}\n")

users = load_data(USERS_FILE)
banned_users = load_data(BANNED_FILE)

# --- 🔥 START COMMAND ---
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id in banned_users:
        return

    if user_id not in users:
        users.add(user_id)
        save_data(USERS_FILE, user_id)

    text = """ 🔥 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐀𝐃𝐔𝐋𝐓 𝐂𝐎𝐋𝐋𝐄𝐂𝐓𝐈𝐎𝐍 𝐔𝐍𝐋𝐎𝐂𝐊𝐄𝐃 🔥

𝐇𝐃 + 𝐔𝐥𝐭𝐫𝐚-𝐅𝐫𝐞𝐬𝐡 𝐕𝐢𝐝𝐞𝐨𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐍𝐨𝐰

💦 𝐌𝐨𝐦-𝐒𝐨𝐧 𝐅𝐚𝐧𝐭𝐚𝐬𝐲
💦 𝐁𝐫𝐨𝐭𝐡𝐞𝐫-𝐒𝐢𝐬𝐭𝐞𝐫 𝐓𝐚𝐛𝐨𝐨
💦 𝐀𝐮𝐧𝐭𝐲 & 𝐁𝐡𝐚𝐛𝐡𝐢 𝐃𝐞𝐬𝐢 𝐇𝐨𝐭
💦 𝐓𝐞𝐞𝐧 𝐈𝐧𝐝𝐢𝐚𝐧 (𝟏𝟖+)
💦 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐑𝐞𝐞𝐥𝐬 𝐒𝐭𝐚𝐫𝐬
💦 𝐃𝐞𝐬𝐢 𝐁𝐡𝐚𝐛𝐡𝐢 & 𝐀𝐮𝐧𝐭𝐲 𝐒𝐞𝐫𝐢𝐞𝐬
💦 𝐅𝐨𝐫𝐞𝐢𝐠𝐧𝐞𝐫 & 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐭𝐢𝐨𝐧𝐚𝐥
💦 𝐇𝐚𝐫𝐝𝐜𝐨𝐫𝐞 & 𝐑𝐨𝐥𝐞𝐩𝐥𝐚𝐲 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧

𝐀𝐥𝐥 𝐂𝐚𝐭𝐞𝐠𝐨𝐫𝐢𝐞𝐬 𝐢𝐧 𝐎𝐧𝐞 𝐏𝐚𝐜𝐤𝐚𝐠𝐞

💎 𝐎𝐧𝐥𝐲 𝐑𝐬 𝟒𝟗₹ 𝐟𝐨𝐫 𝐋𝐢𝐦𝐢𝐭𝐞𝐝 𝐓𝐢𝐦𝐞 💎

✅ 𝐅𝐮𝐥𝐥 𝐇𝐃  𝐐𝐮𝐚𝐥𝐢𝐭𝐲
✅ 𝐈𝐧𝐬𝐭𝐚𝐧𝐭 𝐃𝐞𝐥𝐢𝐯𝐞𝐫𝐲
✅ 𝟏𝟎𝟎% 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 & 𝐔𝐩𝐝𝐚𝐭𝐞𝐝 𝐋𝐢𝐧𝐤𝐬

👇 𝐁𝐔𝐘 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 👇  
"""

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("💎 𝐁𝐔𝐘 𝐏𝐑𝐄𝐌𝐈𝐔𝐌", callback_data="buy"),
        InlineKeyboardButton("🎁 𝐅𝐑𝐄𝐄 𝐃𝐄𝐌𝐎", url="https://t.me/ZOYA_DEMO_BOT?start=BQADAQAD8AoAArpk2Uboq47mJeW5cBYE")
    )
    markup.add(
        InlineKeyboardButton("🛠️ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url="https://t.me/ZOYAXSUPPORT?text=HELLO%20%20MAM%20MUJHE%20PREMIUM%20SUBSCRIPTION%20CHAHIYE")
    )

    try:
        bot.send_photo(
            chat_id=user_id,
            photo="https://kommodo.ai/i/nc5zJIJa4gO94AzXLemD",
            caption=text,
            reply_markup=markup
        )
    except Exception as e:
        print(f"Error sending start photo: {e}")

# --- 💰 BUY BUTTON ---
@bot.callback_query_handler(func=lambda call: call.data == "buy")
def buy(call):
    text = """💎 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐌𝐄𝐌𝐁𝐄𝐑𝐒𝐇𝐈𝐏 💎

📦 Plan: Lifetime  
💰 Price: ₹49  

━━━━━━━━━━━━━━━  
🏦 UPI ID: <code>lakshkar0786@fam</code>  
━━━━━━━━━━━━━━━  

💡 📲 𝐒𝐜𝐚𝐧 𝐭𝐡𝐞 𝐐𝐑 𝐚𝐧𝐝 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞 𝐩𝐚𝐲𝐦𝐞𝐧𝐭

💡 𝐀𝐟𝐭𝐞𝐫 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥 𝐩𝐚𝐲𝐦𝐞𝐧𝐭  
𝐂𝐥𝐢𝐜𝐤 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧 𝐛𝐞𝐥𝐨𝐰 👇
"""
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ 𝐆𝐄𝐓 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐋𝐈𝐍𝐊", callback_data="paid"))

    bot.send_photo(
        chat_id=call.from_user.id,
        photo="https://kommodo.ai/i/CuehIzp2uCq8ju8sykZr",
        caption=text,
        reply_markup=markup
    )
    bot.answer_callback_query(call.id)

# --- ❌ PAYMENT CHECK ---
@bot.callback_query_handler(func=lambda call: call.data == "paid")
def paid(call):
    bot.answer_callback_query(call.id, "❌ Payment not detected")
    bot.send_message(call.from_user.id, "❌ Payment failed. Pehle payment karo phir try karo.")

# --- 📊 ADMIN COMMANDS ---
@bot.message_handler(commands=['stats', 'ban', 'unban', 'broadcast'])
def admin_commands(message):
    if message.from_user.id != ADMIN_ID:
        return

    cmd = message.text.split()[0][1:]

    if cmd == 'stats':
        bot.reply_to(message, f"📊 STATS\n👤 Total: {len(users)}\n🚫 Banned: {len(banned_users)}")
    
    elif cmd == 'broadcast':
        if not message.reply_to_message:
            bot.reply_to(message, "Reply to a message to broadcast!")
            return
        
        success, failed = 0, 0
        for user in users:
            if user in banned_users: continue
            try:
                bot.copy_message(user, message.chat.id, message.reply_to_message.message_id)
                success += 1
            except: failed += 1
        bot.reply_to(message, f"✅ Success: {success}\n❌ Failed: {failed}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Flask ko alag thread mein chalayein
    threading.Thread(target=run_flask, daemon=True).start()
    
    print("🔥 Bot Starting...")
    # Infinity polling with skip_pending to avoid spam on restart
    bot.infinity_polling(skip_pending=True)
    
