<script>
    import { onMount } from "svelte";
    import { createPost, getCategories } from "$lib/api.js";

    let title = "";
    let content = "";
    let category_id = "";
    let categories = [];

    onMount(async () => {
        categories = await getCategories();
    });

    async function submit() {
        await createPost({ title, content, category_id });
        alert("Post created!");
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
