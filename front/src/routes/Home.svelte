<script>
    import { getPosts, getCategories } from "../lib/api.js";
    export let navigate;

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
            <a href="#detail" on:click={() => navigate("detail", { id: p.id })}
                >{p.title}</a
            >
        </li>
    {/each}
</ul>

<h3>Categories</h3>
<ul>
    {#each categories as c}
        <li>
            <a
                href="#category"
                on:click={() => navigate("category", { slug: c.slug })}
                >{c.name}</a
            >
        </li>
    {/each}
</ul>
