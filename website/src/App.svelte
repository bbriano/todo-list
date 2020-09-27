<script>
    let tasks = [];
    let title = "";
    getTasks()

    async function getTasks() {
        const res = await fetch("http://localhost:5000/");
        const data = await res.json();
        tasks = data.tasks
    }

    async function addTask(title) {
        const res = await fetch("http://localhost:5000/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title }),
        });
        getTasks();
    }

    async function toggleTaskCompletion(id) {
        const res = await fetch("http://localhost:5000/", {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id }),
        });
        getTasks();
    }

    async function deleteTask(id) {
        const res = await fetch("http://localhost:5000/", {
            method: "DELETE",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id }),
        });
        getTasks();
    }
</script>

<div class="main">
    <h1>Todo list app</h1>
    <input bind:value={title}/><button on:click={() => addTask(title); title=""}>Add</button>
    {#each tasks as task}
        <p>
            <input
                type="checkbox"
                checked={task.completed}
                on:click={() => toggleTaskCompletion(task.id)}
            />
            {task.title}
            <button on:click={() => deleteTask(task.id)}>X</button>
        </p>
    {/each}
</div>

<style>
    .main {
        padding: 1rem;
        margin: 0 auto;
        max-width: 640px;
    }

    h1 {
        color: #6611ff;
    }
</style>
