<nav>
    <a href="/">🏠 Home</a>
    <a href="/postform">📝 New Post</a>
    <a href="/categoryform">📝 New Category</a>
</nav>

<main>
    <slot></slot>
</main>

<style>
    body {
        font-family: sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
        color: #333;
    }

    nav {
        background-color: #333;
        padding: 1rem;
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    nav a {
        color: white;
        text-decoration: none;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    nav a:hover {
        background-color: #575757;
    }

    main {
        max-width: 900px;
        margin: 2rem auto;
        padding: 1.5rem;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
</style>
