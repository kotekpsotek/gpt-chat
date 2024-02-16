<script setup lang="ts">
    import { ref, defineProps } from 'vue';

    let myId = "desc";

    const question = ref("");
    const answer = ref("");

    // define props using a type literal
    const props = defineProps({
        api: {
            type: String,
            required: true
        }
    })

    async function sendQuestion() {
        const apiUrl = new URL(props.api);
        apiUrl.pathname = "/question"
        console.log(apiUrl.toString())
        
        const f = await fetch(apiUrl.toString(), {
            method: "POST",
            headers: {
                'content-type': "application/json"
            },
            body: JSON.stringify({ question: question.value })
        });

        if (f.status == 200) {
            const { answer: a } = (await f.json())
            answer.value = a
        }
        else alert("Cannot make request for datas!");
    }
</script>

<template>
    <div>
        <h1>Chat with GPT</h1>
        <p :id="myId">I'm happy to let you clear a unclear!</p>
        <input type="text" placeholder="How can i help you?" v-model="question">
        <button @click="sendQuestion">Ask</button>
    </div>
    <div class="answer" v-if="answer.length">
        <p>{{ answer }}</p>
    </div>
</template>