<script>
    import Router, { link } from "svelte-spa-router";
    import Home from "./routes/Home.svelte";
    import Category from "./routes/Category.svelte";
    import PostDetail from "./routes/PostDetail.svelte";
    import PostForm from "./routes/PostForm.svelte";

    const routes = {
        "/": Home,
        "/category/:slug": Category,
        "/post/:id": PostDetail,
        "/new": PostForm,
    };
</script>

<nav>
    <a href="/" use:link>🏠 Home</a>
    <a href="/new" use:link>📝 New Post</a>
</nav>

<Router {routes} />
