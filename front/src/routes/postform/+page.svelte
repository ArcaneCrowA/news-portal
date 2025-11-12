<script>
    import { onMount } from "svelte";
    import { createPost, getCategories } from "$lib/api.js";
    import { goto } from "$app/navigation";

    let title = "";
    let content = "";
    let category_id = "";
    let categories = [];

    onMount(async () => {
        categories = await getCategories();
    });

    async function submit() {
        await createPost({ title, content, category_id });
        goto("/");
    }
</script>

<h2>New Post</h2>
<form on:submit|preventDefault={submit}>
    <input bind:value={title} placeholder="Title" required />
    <select bind:value={category_id}>
        <option value="">Select category</option>
        {#each categories as c}
            <option value={c.id}>{c.name}</option>
        {/each}
    </select>
    <textarea bind:value={content} placeholder="Content"></textarea>
    <button type="submit">Create</button>
</form>

<style>
    h2 {
        color: #333;
        margin-bottom: 1.5rem;
        text-align: center;
    }

    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        max-width: 500px;
        margin: 0 auto;
        padding: 2rem;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    }

    input[type="text"],
    textarea,
    select {
        width: 100%;
        padding: 12px;
        border: 1px solid #ced4da;
        border-radius: 5px;
        font-size: 1em;
        box-sizing: border-box; /* Ensures padding doesn't increase width */
    }

    input[type="text"]:focus,
    textarea:focus,
    select:focus {
        border-color: #007bff;
        outline: none;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }

    textarea {
        min-height: 120px;
        resize: vertical;
    }

    button[type="submit"] {
        background-color: #007bff;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }

    button[type="submit"]:hover {
        background-color: #0056b3;
    }
</style>
