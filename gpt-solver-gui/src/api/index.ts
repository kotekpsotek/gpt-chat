interface Question {
    question: string,
    answer: string,
    date_timestamp: number
}

type QuestionList = Question[];

export interface QuestionsStorage {
    questions: QuestionList
}

export default class API {
    /**
     * @description Get all questions from persistant storage
    */
    static getStorageQuestions(): QuestionsStorage {
        const questions = localStorage.getItem("gpt-solver-questions")

        if (!questions) return { questions: [] };

        const deserialized = JSON.parse(questions) as QuestionsStorage;

        return deserialized;
    }

    /**
     * @description Save all questions to persisatnt storage
     * @param questions 
     * @returns 
     */
    static setStorageQuestions(questions: QuestionsStorage): boolean {
        try {
            const serialized = JSON.stringify(questions);
    
            const _save = localStorage.setItem("gpt-solver-questions", serialized);
            
            return true;
        }
        catch(err) {
            // Log
            console.error(err);

            // .. Return
            return false;
        }
    }
}