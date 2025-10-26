<h1 align="center">🏕️ Survivor in the Wilderness</h1>

<p align="center">
  <b>A Python text-based adventure game where your choices determine your survival in the wild.</b><br>
  <i>Explore, hunt, cook, collect, and survive through danger — one decision at a time.</i>
</p>

---

<h2>📘 Overview</h2>

<p>
<strong>Survivor in the Wilderness</strong> is a fully interactive <strong>text-based adventure game</strong> written in Python.  
The game immerses players in a wilderness survival story, where each decision affects your fate — gather resources, fight animals, explore mysterious locations, and uncover secrets.
</p>

---

<h2>🎯 Objective</h2>

<p>
Your goal is to <strong>survive through an entire day in the wild</strong> by making smart choices.  
Every location you explore gives opportunities or dangers — gather items, hunt deer, cook meals, and face the ultimate challenge: <strong>the wild grizzly bear.</strong>
</p>

---

<h2>🧩 Features</h2>

<ul>
  <li>🌳 Explore multiple locations (Forest, River, Lake, Woodlands, and more)</li>
  <li>🪓 Collect items and build your inventory dynamically</li>
  <li>🔥 Craft fires, cook food, and regain health</li>
  <li>🎯 Hunt animals like deer and fish for survival</li>
  <li>🐻 Face the final boss — a dangerous grizzly bear</li>
  <li>💬 Text-based interface with typing effect for immersion</li>
  <li>🎮 Replayable — every run can lead to different outcomes</li>
</ul>

---

<h2>📂 Folder Structure</h2>

<pre>
Survivor-In-The-Wilderness/
│
├── main.py                  # Main game script
├── README.md                # Project documentation
└── LICENSE                  # MIT License (optional)
</pre>

---

<h2>⚙️ Setup & Run Instructions</h2>

<p>To play the game on your own system:</p>

<ol>
  <li>Make sure you have <strong>Python 3</strong> installed.</li>
  <li>Download or clone this repository:</li>
</ol>

<pre><code>git clone https://github.com/your-username/Survivor-In-The-Wilderness.git</code></pre>

<ol start="3">
  <li>Navigate into the project folder:</li>
</ol>

<pre><code>cd Survivor-In-The-Wilderness</code></pre>

<ol start="4">
  <li>Run the game using:</li>
</ol>

<pre><code>python main.py</code></pre>

<p><i>Once launched, follow the text prompts to play and make your decisions wisely!</i></p>

---

<h2>🧠 Game Mechanics & Logic</h2>

<p>Here’s how the key systems work behind the scenes:</p>

<ul>
  <li><b>Player Stats:</b> Health and damage dynamically change based on actions and inventory.</li>
  <li><b>Inventory System:</b> Items like apples, fire starters, fishing lines, and weapons affect gameplay.</li>
  <li><b>Choice-based Progression:</b> Player input determines the story’s flow — explore, rest, or battle.</li>
  <li><b>Combat System:</b> Uses Python’s <code>random</code> library to simulate variable damage outcomes.</li>
  <li><b>Typewriter Effect:</b> Achieved via <code>sys.stdout</code> and <code>time.sleep()</code> to enhance immersion.</li>
</ul>

---

<h2>💻 Key Libraries Used</h2>

<ul>
  <li><code>random</code> – for generating random damage and outcomes</li>
  <li><code>sys</code> – for text typing and output control</li>
  <li><code>time</code> – to control pacing and timing</li>
  <li><code>os</code> – to clear the console for smoother flow</li>
</ul>

---

<h2>🎮 Gameplay Preview</h2>

<pre>
Before we begin, please Enter Your Name:
> Sheikh

Welcome Player 'Sheikh' to the 'Survivor In The Wilderness' Game

Would you like to start the game? (Yes or No):
> yes

Dropping you into the game now...
...
You've just woken up in the wilderness at 5AM...
What will you do first?
</pre>

---

<h2>🏕️ Progression Path</h2>

<ol>
  <li><b>Morning:</b> Explore the forest or river to gather essentials.</li>
  <li><b>Midday:</b> Hunt deer and gather food for survival.</li>
  <li><b>Afternoon:</b> Fish at the lake and collect useful tools.</li>
  <li><b>Evening:</b> Cook, rest, and explore the woodlands.</li>
  <li><b>Nightfall:</b> Survive the grizzly bear encounter to win the game.</li>
</ol>

---

<h2>🏆 Win Condition</h2>

<p>
Defeat the grizzly bear in combat and survive the night.  
The game ends with a twist — another survivor emerges… but are they friend or foe?
</p>

---

<h2>📸 Example Inventory Progression</h2>

<pre>
['Fire Starter', 'Bow and Arrow', 'Cooked Fish', 'Apple', 'Lost Hatchet']
</pre>

---

<h2>🚀 Future Improvements</h2>

<ul>
  <li>Add save/load functionality</li>
  <li>Include a GUI version with <code>tkinter</code> or <code>pygame</code></li>
  <li>Implement difficulty levels</li>
  <li>Expand storyline with new biomes and choices</li>
</ul>

---

<h2>🧾 License</h2>

<p>
This project is licensed under the <strong><a href="https://opensource.org/licenses/MIT">MIT License</a></strong> — feel free to use, modify, and distribute.
</p>

---

<h2>💬 Author</h2>

<p>
Developed with ❤️ by <strong>Sheikh</strong><br>
<i>“Survival is about choices — make yours count.”</i>
</p>
