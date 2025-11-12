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
