import { defineStore } from 'pinia';
import { DateTime } from 'luxon';

interface ConversationTurn {
  input: string;
  input_datetime?: DateTime;
  reply?: string;
  reply_datetime?: DateTime;
}

export const useConversationTurnsStore = defineStore('conversation-turns', {
  state: () => ({
    turns: [] as ConversationTurn[],
  }),
  getters: {
    getTurns: (state) => state.turns,
  },
  actions: {
    addInputTurn(input: string) {
      this.turns.push({
        input,
        input_datetime: DateTime.now(),
        reply: '',
      });
      return this.turns.length - 1;
    },
    appendReplyFragmentToTurn(fragment: string, turn_index: number) {
      this.turns[turn_index].reply += fragment;
      this.turns[turn_index].reply_datetime = DateTime.now();
    },
  },
});