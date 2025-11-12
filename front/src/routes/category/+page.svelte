<script>
    import { onMount } from "svelte";
    import { page } from "$app/stores";
    import { getCategoryPosts, getCategories } from "$lib/api.js";

    let posts = [];
    let categories = [];
    let loading = true;
    let error = null;
    let slug;

    $: {
        slug = $page.params.slug;
        load();
    }

    // load posts for the category
    async function load() {
        loading = true;
        error = null;
        try {
            posts = await getCategoryPosts(slug);
            categories = await getCategories();
        } catch (e) {
            error = "Failed to load category posts.";
            console.error(e);
        } finally {
            loading = false;
        }
    }
</script>

<nav>
    <a href="/">← Home</a>
</nav>

{#if loading}
    <p>Loading posts for “{slug}”…</p>
{:else if error}
    <p class="error">{error}</p>
{:else}
    <h2>Category: {slug}</h2>

    {#if posts.length === 0}
        <p>No posts in this category yet.</p>
    {:else}
        <ul>
            {#each posts as p}
                <li>
                    <a href="/post/{p.id}">{p.title}</a>
                    <div>
                        <small>{new Date(p.created_at).toLocaleString()}</small>
                    </div>
                </li>
            {/each}
        </ul>
    {/if}

    <aside>
        <h3>All categories</h3>
        <ul>
            {#each categories as c}
                <li>
                    <a href="/category/{c.slug}">{c.name}</a>
                </li>
            {/each}
        </ul>
    </aside>
{/if}

<style>
    nav {
        margin-bottom: 1rem;
    }
    .error {
        color: darkred;
    }
    ul {
        list-style: none;
        padding: 0;
    }
    li {
        margin-bottom: 0.75rem;
    }
    a {
        color: inherit;
        text-decoration: underline;
        cursor: pointer;
    }
    aside {
        margin-top: 1.5rem;
        border-top: 1px solid #eee;
        padding-top: 1rem;
    }
</style>
