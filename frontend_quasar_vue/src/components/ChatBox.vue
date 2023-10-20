<template>
    <div
        class="chatbox q-pa-md q-gutter-md column flex-center"
    >
        <div class="message-container q-pa-md q-ma-none bg-white shadow-1">
            <div
                class="message-window"
            >
                <q-chat-message
                    label="Chat confidentially with your data"
                />
                <template
                    v-for="(turn, index) in conversation_turns"
                    :key="index"
                >
                    <q-chat-message
                        v-if="!!turn.input"
                        :text="[turn.input]"
                        :stamp="turn.input_datetime && turn.input_datetime.toRelative() || ''"
                        sent
                    />
                    <q-chat-message
                        v-if="!!turn.reply"
                        :text="[turn.reply]"
                        :stamp="turn.reply_datetime && turn.reply_datetime.toRelative() || ''"
                    />
                    <q-chat-message
                        v-if="!turn.reply"
                    >
                        <DotsLoader />
                    </q-chat-message>
                </template>
            </div>
        </div>

        <div class="input-container row q-ma-md">
            <q-input
                v-model.trim="input_message"
                outlined
                flat
                dense
                placeholder="Type a message..."
                class="col q-mr-sm shadow-1"
            />
            <q-btn
                unelevated
                text-color="blue-10"
                icon="send"
                class="col-1"
                :disable="!input_message"
                @click="sendMessage"
            />
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import { DateTime } from 'luxon';
import DotsLoader from './DotsLoader.vue';

const VITE_API_BASE_URL = import.meta.env.VITE_API_BASE_URL as string;

interface ConversationTurn {
    input: string;
    input_datetime?: DateTime;
    reply?: string;
    reply_datetime?: DateTime;
}

const conversation_turns: Array<ConversationTurn> = reactive([
    {
        input: '',
        reply: 'How can I help you today?',
        reply_datetime: DateTime.now()
    }
])

const input_message = ref<string>('');

async function sendMessage() {
    const next_turn_index = conversation_turns.length;
    const input = input_message.value;
    conversation_turns.push({
        input: input,
        input_datetime: DateTime.now()
    })
    input_message.value = '';
    const ws = new WebSocket(`ws://${VITE_API_BASE_URL}/chat`);
    ws.addEventListener('event', (event: MessageEvent<string>) => {
        const reply_chunk = event.data;
        conversation_turns[next_turn_index].reply += reply_chunk;
        conversation_turns[next_turn_index].reply_datetime = DateTime.now();
    })
    ws.send(input);
}

</script>

<style lang="scss">
.chatbox {
    width: 100%;

    .message-container {
        width: 100%;
    }
    .input-container {
        width: 100%;
    }
}
</style>
