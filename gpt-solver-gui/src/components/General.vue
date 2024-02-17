<script setup lang="ts">
    import { ref, defineProps } from 'vue';
    import Answering from "../assets/answering.svg";
    import BotProfile from "../assets/bot_profile.jpg";
    import { QuestionsStorage } from '../api';

    let myId = "desc";

    const question = ref("");
    const answer = ref("");
    const durningAnswering = ref(false);

    // define props using a type literal
    const props = defineProps<{
        api: string,
        questions: QuestionsStorage
    }>()

    async function sendQuestion() {
        try { 
            durningAnswering.value = true;
            answer.value = "";
    
            props.questions.questions.push({
                date_timestamp: Date.now(),
                answer: "Test answer: I have recived your question!",
                question: question.value
            })
            
           /*  const apiUrl = new URL(props.api);
            apiUrl.pathname = "/question"
            
            const f = await fetch(apiUrl.toString(), {
                method: "POST",
                headers: {
                    'content-type': "application/json"
                },
                body: JSON.stringify({ question: question.value })
            });
    
            if (f.status == 200) {
                const { answer: a } = (await f.json())

                // Add answer for answer field
                answer.value = a

                // Add question to questions list (for Timeline)
                props.questions.questions.push({
                    date_timestamp: Date.now(), // Date from answer time
                    answer: a,
                    question: question.value
                });
            }
            else alert("Cannot make request for datas!");
    
            durningAnswering.value = false; */
        }
        catch(err) {
            durningAnswering.value = false;
        }
    }
</script>

<template>
    <div class="wrapper w-screen h-screen flex flex-col gap-4 justify-center items-center">
        <div class="card w-3/5">
            <h1 class="text-2xl font-semibold">Chat with GPT</h1>
            <p :id="myId" class="font-protestRiot text-gray-500">I'm happy to let you clear a unclear!</p>
            <div id="trigger" class="flex flex-col gap-2 mt-3">
                <textarea id="question" class="bg-slate-200 p-2 rounded-sm" style="resize: none;" placeholder="How do you feel?" cols="30" rows="10" wrap="soft" v-model="question">
                </textarea>
                <button @click="sendQuestion" class="w-full p-2 text-black font-semibold border-2 border-black rounded-md hover:bg-black hover:text-white transition-all duration-150">Ask</button>
            </div>
        </div>
        <div v-if="durningAnswering" class="flex gap-x-2">
            <p>Answering</p>
            <img v-bind:src="Answering" alt="Loading...">
        </div>
        <div class="card w-3/5" v-if="answer.length">
            <div class="flex items-start justify-start">
                <img :src="BotProfile" class="rounded-full" width="40px" height="40px">
                <div id="answer" class="flex items-center overflow-y-auto" style="max-height: 200px;">
                    <p>{{ answer }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
