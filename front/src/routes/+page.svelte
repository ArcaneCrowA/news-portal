<script>
    import { onMount } from "svelte";
    import { getPosts, getCategories } from "$lib/api.js";

    let posts = [];
    let categories = [];

    onMount(async () => {
        posts = await getPosts();
        categories = await getCategories();
    });
</script>

<h2>Recent Posts</h2>
<ul>
    {#each posts as p}
        <li>
            <a href="/posts/{p.id}">{p.title}</a>
        </li>
    {/each}
</ul>

<h3>Categories</h3>
<ul>
    {#each categories as c}
        <li>
            <a href="/category/{c.slug}">{c.name}</a>
        </li>
    {/each}
</ul>

<style>
    h2,
    h3 {
        color: #333;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #eee;
        padding-bottom: 0.5rem;
    }

    ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    li {
        background-color: #f9f9f9;
        margin-bottom: 0.75rem;
        padding: 1rem 1.5rem;
        border-radius: 6px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease-in-out;
    }

    li:hover {
        transform: translateY(-3px);
    }

    li a {
        text-decoration: none;
        color: #007bff;
        font-weight: 600;
        font-size: 1.1em;
        display: block; /* Make the whole list item clickable area */
    }

    li a:hover {
        color: #0056b3;
    }
</style>
