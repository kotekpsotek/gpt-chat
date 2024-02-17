<script setup lang="ts">
    import { defineProps } from 'vue';
    import { QuestionsStorage } from "../api";
    import { displayHistoricalQuestion } from "../api/reactivity";
    import TimeAgo from "javascript-time-ago"
    import en from "javascript-time-ago/locale/en";

    const props = defineProps<{
        singleQuestion: QuestionsStorage["questions"][0]
    }>();

    // Date formatting
    TimeAgo.addDefaultLocale(en);
    const localeLanguages = navigator.languages;
    const formatterDate = new TimeAgo(localeLanguages[0]);

    function handleClick() {
        // Hide or show selected question
        if (displayHistoricalQuestion.value.whichDisplay && displayHistoricalQuestion.value.whichDisplay?.date_timestamp != props.singleQuestion.date_timestamp && displayHistoricalQuestion.value.display) {
            displayHistoricalQuestion.value.display = true; // this is only for explicity mark as not hidden
        }
        else {
            displayHistoricalQuestion.value.display = !displayHistoricalQuestion.value.display;
        }

        if (displayHistoricalQuestion.value.display) {
            displayHistoricalQuestion.value.whichDisplay = props.singleQuestion;
        }
        else displayHistoricalQuestion.value.whichDisplay = undefined;
    }
</script>

<template>
    <div id="question" class="flex justify-between w-full" @click="handleClick">
        <p class="max-w-2/5 truncate">{{ props.singleQuestion.question }}</p>
        <p id="time-difference" class="text-xs text-gray-700 text-end">{{ formatterDate.format(props.singleQuestion.date_timestamp) }}</p>
    </div>
</template>