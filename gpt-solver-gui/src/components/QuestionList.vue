<!-- 
    Here will be:
        - Displaying user questions in abreviation, with ability to switch to full'em
    Must exists:
        - Storage to load and update question (persiatant storage)
-->

<script setup lang="ts">
    import Question from "./Question.vue";
    import type { QuestionsStorage } from "../api";

    const props = defineProps<{
        questions: QuestionsStorage,
    }>()
</script>

<template>
    <div class="card bg-slate-200 mr-2 h-4/5 relative overflow-hidden" style="width: 300px;">
        <h1 class="text-lg font-semibold">Timeline</h1>
        <div class="mt-2 overflow-y-auto h-full flex flex-col gap-y-2" v-if="props.questions.questions.length">
            <Question :single-question="questionSingle" v-for="questionSingle in props.questions.questions"/>
        </div>
        <div class="absolute top-1/2 left-0 w-full" v-else-if="!props.questions.questions.length">
            <p class="text-center text-slate-400">You haven't any questions</p>
        </div>
    </div>
</template>