<!-- 
    Here will be:
        - Displaying user questions in abreviation, with ability to switch to full'em
    Must exists:
        - Storage to load and update question (persiatant storage)
-->

<script setup lang="ts">
    import type { QuestionsStorage } from "../api";

    const props = defineProps<{
        questions: QuestionsStorage,
    }>()
</script>

<template>
    <div class="card h-4/5 relative" style="width: 300px;">
        <h1 class="text-lg font-semibold">Timeline</h1>
        <div v-if="props.questions.questions.length" v-for="{ question, answer, date_timestamp } in props.questions.questions">

        </div>
        <div class="absolute top-1/2 left-0 w-full" v-else-if="!props.questions.questions.length">
            <p class="text-center text-slate-400">You haven't any questions</p>
        </div>
    </div>
</template>