<script setup lang="ts">
    import { ref, defineProps } from 'vue';
    import Answering from "../assets/answering.svg";
    import BotProfile from "../assets/bot_profile.jpg";
    import APIStorage, { QuestionsStorage } from '../api';
    import { displayHistoricalQuestion } from '../api/reactivity';

    let myId = "desc";

    const question = ref("");
    const answer = ref("");
    const durningAnswering = ref(false);
    const interactionFieldsDisabled = ref(false);

    // define props using a type literal
    const props = defineProps<{
        api: string,
        questions: QuestionsStorage
    }>()

    async function sendQuestion() {
        if (question.value.length) {
            try {
                // Disable giving question by answer will have come
                interactionFieldsDisabled.value = true;
    
                // That App is durning answering
                durningAnswering.value = true;
    
                // Clear previous answer stage what also will cause hideing that
                answer.value = "";
                
                const apiUrl = new URL(props.api);
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
                    props.questions.questions.unshift({
                        date_timestamp: Date.now(), // Date from answer time
                        answer: a,
                        question: question.value
                    });
    
                    // FIXME: Only for test purposes. Pass on a first place new question on questions list 
                    /* props.questions.questions.unshift({
                        date_timestamp: Date.now(),
                        answer: "Test answer: I have recived your question!",
                        question: question.value
                    }) */
     
                }
                else alert("Cannot make request for datas!");
        
                durningAnswering.value = false;
    
                // FIXME: Only for test cases
                /* setTimeout(() => {
                    interactionFieldsDisabled.value = false;
                }, 5_000) */
    
                // Make interaction field enabled again
                interactionFieldsDisabled.value = false;  
    
                // Resave Questions
                APIStorage.setStorageQuestions(props.questions);
            }
            catch(err) {
                // Signal, isn't durning answering process
                durningAnswering.value = false;
    
                // Make interaction field enabled again
                interactionFieldsDisabled.value = false;  
            }
        }
        else alert("Ohhh noooo! You did not ask about anything!")
    }
</script>

<template>
    <div class="wrapper w-screen h-screen flex flex-col gap-4 justify-center items-center">
        <div class="card w-3/5">
            <h1 class="text-2xl font-semibold">Chat with GPT</h1>
            <p :id="myId" class="font-protestRiot text-gray-500">I'm happy to let you clear a unclear!</p>
            <div id="trigger" class="flex flex-col gap-2 mt-3">
                <textarea id="question" class="bg-slate-200 p-2 rounded-sm disabled:cursor-none" style="resize: none;" placeholder="How do you feel?" cols="30" rows="10" wrap="soft" v-model="question" :disabled="interactionFieldsDisabled">
                </textarea>
                <button @click="sendQuestion" class="w-full p-2 text-black font-semibold border-2 border-black rounded-md hover:bg-black hover:text-white transition-all duration-150 disabled:cursor-not-allowed disabled:opacity-80" :disabled="interactionFieldsDisabled">Ask</button>
            </div>
        </div>
        <div v-if="durningAnswering" class="flex gap-x-2">
            <p>Answering</p>
            <img v-bind:src="Answering" alt="Loading...">
        </div>
        <div class="card w-3/5" v-if="answer.length || displayHistoricalQuestion.display">
            <div class="flex items-start justify-start">
                <img :src="BotProfile" class="rounded-full" width="40px" height="40px">
                <div id="answer" class="flex items-center overflow-y-auto" style="max-height: 200px;">
                    <p>{{ answer.length ? answer : displayHistoricalQuestion.whichDisplay }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
