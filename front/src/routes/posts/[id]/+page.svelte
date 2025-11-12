<script>
    import { onMount } from "svelte";
    import { page } from "$app/stores";
    import { getPost, getComments, addComment } from "$lib/api.js";

    let post = {};
    let comments = [];
    let newComment = "";
    let id;

    $: {
        id = $page.params.id;
        load();
    }

    async function load() {
        post = await getPost(id);
        comments = await getComments(id);
    }

    async function submitComment() {
        await addComment({ post_id: id, content: newComment });
        comments = await getComments(id);
        newComment = "";
    }
</script>

<h2>{post.title}</h2>
<p>{post.content}</p>

<h3>Comments</h3>
<ul>
    {#each comments as c}
        <li>{c.content}</li>
    {/each}
</ul>

<textarea bind:value={newComment}></textarea>
<button on:click={submitComment}>Add Comment</button>
