import { ref } from "vue";
import type { QuestionsStorage } from ".";

export const displayHistoricalQuestion = ref<{
    display: boolean,
    whichDisplay?: QuestionsStorage["questions"][0]
}>({ display: false })
