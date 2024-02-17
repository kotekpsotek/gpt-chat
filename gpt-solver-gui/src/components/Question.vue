<script setup lang="ts">
    import { defineProps } from 'vue';
    import { QuestionsStorage } from "../api";
    import TimeAgo from "javascript-time-ago"
    import en from "javascript-time-ago/locale/en";

    const props = defineProps<{
        singleQuestion: QuestionsStorage["questions"][0]
    }>();
    

    // Date formatting
    TimeAgo.addDefaultLocale(en);
    const localeLanguages = navigator.languages;
    const formatterDate = new TimeAgo(localeLanguages[0]);
</script>

<template>
    <div id="question" class="flex justify-between w-full">
        <p class="max-w-2/5 truncate">{{ props.singleQuestion.question }}</p>
        <p id="time-difference" class="text-xs text-gray-700 text-end">{{ formatterDate.format(props.singleQuestion.date_timestamp) }}</p>
    </div>
</template>