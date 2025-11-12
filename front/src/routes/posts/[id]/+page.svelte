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

<textarea bind:value={newComment} placeholder="Add a comment..."></textarea>
<button on:click={submitComment}>Add Comment</button>

<style>
    h2 {
        color: #333;
        margin-bottom: 1rem;
    }

    p {
        color: #555;
        line-height: 1.6;
        margin-bottom: 2rem;
    }

    h3 {
        color: #333;
        margin-top: 2.5rem;
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
        background-color: #e9ecef;
        margin-bottom: 0.75rem;
        padding: 1rem 1.25rem;
        border-radius: 6px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        font-size: 0.95em;
        color: #444;
    }

    textarea {
        width: 100%;
        padding: 10px;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box; /* Ensures padding doesn't increase width */
        font-family: sans-serif;
        font-size: 1em;
        min-height: 80px;
    }

    textarea:focus {
        border-color: #007bff;
        outline: none;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }

    button {
        background-color: #007bff;
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #0056b3;
    }
</style>
