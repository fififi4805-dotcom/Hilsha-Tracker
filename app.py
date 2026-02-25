<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hilsha Helper</title>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
<style>
    :root {
        --navy: #001f3f;
        --light: #f9f9f9;
        --dark: #121212;
        --primary-text-light: #ffffff;
        --primary-text-dark: #000000;
        --highlight: #ffcc00;
    }

    body {
        margin: 0;
        font-family: 'Roboto', sans-serif;
        background-color: var(--light);
        color: var(--primary-text-dark);
        transition: background-color 0.3s, color 0.3s;
    }

    body.dark-mode {
        background-color: var(--dark);
        color: var(--primary-text-light);
    }

    header {
        background-color: var(--navy);
        color: white;
        padding: 15px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    header h1 {
        margin: 0;
        font-size: 24px;
    }

    .toggle-mode {
        cursor: pointer;
        padding: 8px 12px;
        border: none;
        background-color: var(--highlight);
        border-radius: 5px;
        font-weight: bold;
    }

    nav {
        background-color: #004080;
        display: flex;
        justify-content: space-around;
        padding: 10px 0;
    }

    nav a {
        color: white;
        text-decoration: none;
        font-weight: 500;
        padding: 6px 12px;
        border-radius: 4px;
        transition: background-color 0.2s;
    }

    nav a:hover {
        background-color: #003366;
    }

    main {
        padding: 20px;
        max-width: 900px;
        margin: auto;
    }

    section {
        margin-bottom: 40px;
    }

    section h2 {
        color: var(--navy);
        border-bottom: 2px solid var(--highlight);
        padding-bottom: 5px;
    }

    input, button, select {
        padding: 10px;
        margin: 5px 0;
        width: 100%;
        max-width: 400px;
        font-size: 16px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }

    button {
        background-color: var(--navy);
        color: white;
        border: none;
        cursor: pointer;
        transition: background-color 0.2s;
    }

    button:hover {
        background-color: #003366;
    }

    .hilsha-result {
        margin-top: 10px;
        padding: 10px;
        background-color: #e6f0ff;
        border-left: 5px solid var(--navy);
        border-radius: 5px;
    }

    .dark-mode .hilsha-result {
        background-color: #001f33;
    }

    ul {
        padding-left: 20px;
    }

    footer {
        text-align: center;
        padding: 15px;
        background-color: #001f3f;
        color: white;
        margin-top: 40px;
    }

</style>
</head>
<body>

<header>
    <h1>Hilsha Helper</h1>
    <button class="toggle-mode">Dark Mode</button>
</header>

<nav>
    <a href="#tips">মাছ কেনার টিপস</a>
    <a href="#location">ঘাট লোকেশন</a>
    <a href="#benefits">ইলিশ খাওয়ার উপকারিতা</a>
    <a href="#complaint">অভিযোগ</a>
</nav>

<main>
    <!-- Hilsha Dam Checker -->
    <section id="tips">
        <h2>মাছ কেনার টিপস</h2>
        <p>ইলিশ কিনতে গেলে এই বিষয়গুলো লক্ষ্য করুন:</p>
        <ul>
            <li>ডিমধারী ইলিশ কিনুন সুস্থ ও তাজা হওয়া উচিত।</li>
            <li>চোখ পরিষ্কার এবং উজ্জ্বল হওয়া দরকার।</li>
            <li>দাম যাচাই করতে বিক্রেতার সাথে তুলনা করুন।</li>
        </ul>
        <label for="price">দাম যাচাই করুন (প্রতি কেজি):</label>
        <input type="number" id="price" placeholder="দাম লিখুন">
        <button onclick="checkPrice()">দাম যাচাই</button>
        <div class="hilsha-result" id="price-result"></div>
    </section>

    <!-- Ghats -->
    <section id="location">
        <h2>ঘাটের লোকেশন</h2>
        <p>বিভিন্ন জেলার ইলিশ ঘাটের নাম এবং লোকেশন:</p>
        <ul>
            <li>মুন্সিগঞ্জ ঘাট: Google Map লিংক</li>
            <li>বরিশাল ঘাট: Google Map লিংক</li>
            <li>কক্সবাজার ঘাট: Google Map লিংক</li>
        </ul>
    </section>

    <!-- Benefits -->
    <section id="benefits">
        <h2>ইলিশ খাওয়ার উপকারিতা</h2>
        <ul>
            <li>মস্তিষ্কের বিকাশে সহায়ক।</li>
            <li>হৃদরোগের ঝুঁকি কমায়।</li>
            <li>প্রোটিন ও ওমেগা-৩ ফ্যাটি অ্যাসিডে সমৃদ্ধ।</li>
        </ul>
    </section>

    <!-- Complaint -->
    <section id="complaint">
        <h2>অভিযোগ</h2>
        <p>কোনও অসুবিধা বা অভিযোগ থাকলে নিচে লিখুন:</p>
        <textarea id="complaint-text" rows="4" placeholder="আপনার অভিযোগ লিখুন"></textarea>
        <button onclick="submitComplaint()">জমা দিন</button>
    </section>
</main>

<footer>
    &copy; 2026 Hilsha Helper | All Rights Reserved
</footer>

<script>
    // Dark/Light mode toggle
    const toggleBtn = document.querySelector('.toggle-mode');
    toggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        toggleBtn.textContent = document.body.classList.contains('dark-mode') ? 'Light Mode' : 'Dark Mode';
    });

    // Price checker (example logic)
    function checkPrice() {
        const price = document.getElementById('price').value;
        const resultDiv = document.getElementById('price-result');
        if (!price) {
            resultDiv.textContent = 'দয়া করে একটি দাম লিখুন।';
            return;
        }
        const marketPrice = 1200; // Example: standard market price
        if (price < marketPrice) {
            resultDiv.textContent = 'দাম কম, ভাল।';
        } else if (price === marketPrice) {
            resultDiv.textContent = 'দাম ঠিক আছে।';
        } else {
            resultDiv.textContent = 'দাম বেশি, সাবধান।';
        }
    }

    // Complaint submission (example)
    function submitComplaint() {
        const text = document.getElementById('complaint-text').value;
        if (!text) {
            alert('অভিযোগ লিখুন।');
            return;
        }
        alert('আপনার অভিযোগ জমা হয়েছে। ধন্যবাদ।');
        document.getElementById('complaint-text').value = '';
    }
</script>

</body>
</html>
