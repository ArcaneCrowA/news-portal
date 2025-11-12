<script>
    import Home from "./routes/Home.svelte";
    import Category from "./routes/Category.svelte";
    import PostDetail from "./routes/PostDetail.svelte";
    import PostForm from "./routes/PostForm.svelte";

    let route = "home";
    let params = {};

    const navigate = (r, p = {}) => {
        route = r;
        params = p;
    };
</script>

<nav>
    <button on:click={() => navigate("home")}>🏠 Home</button>
    <button on:click={() => navigate("new")}>📝 New Post</button>
</nav>

{#if route === "home"}
    <Home on:navigate={(e) => navigate(e.detail.route, e.detail.params)} />
{:else if route === "category"}
    <Category
        slug={params.slug}
        on:navigate={(e) => navigate(e.detail.route, e.detail.params)}
    />
{:else if route === "detail"}
    <PostDetail id={params.id} />
{:else if route === "new"}
    <PostForm />
{/if}
