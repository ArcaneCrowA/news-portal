<script>
    import { onMount, createEventDispatcher } from "svelte";
    import { getCategoryPosts, getCategories } from "../lib/api.js";

    export let slug;
    const dispatch = createEventDispatcher();

    let posts = [];
    let categories = [];
    let loading = true;
    let error = null;

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

    // when slug changes, reload
    $: if (slug) {
        load();
    }

    function goHome() {
        dispatch("navigate", { route: "home", params: {} });
    }

    function openPost(id) {
        dispatch("navigate", { route: "detail", params: { id } });
    }
</script>

<nav>
    <button on:click={goHome}>← Home</button>
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
                    <a href="#" on:click|preventDefault={() => openPost(p.id)}
                        >{p.title}</a
                    >
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
                    <a
                        href="#category"
                        on:click|preventDefault={() =>
                            dispatch("navigate", {
                                route: "category",
                                params: { slug: c.slug },
                            })}
                    >
                        {c.name}
                    </a>
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
