<script>
    import { createCategory } from "$lib/api.js";
    import { goto } from "$app/navigation";

    let name = "";
    let slug = "";

    async function handleSubmit() {
        await createCategory({ name, slug });
        goto("/");
    }
</script>

<h2>New Category</h2>
<form on:submit|preventDefault={handleSubmit}>
    <input bind:value={name} placeholder="Name" required />
    <input bind:value={slug} placeholder="Slug" required />
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
