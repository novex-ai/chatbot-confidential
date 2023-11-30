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
                    v-for="(turn, index) in conversation_turns_store.getTurns"
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
                v-model="input_message"
                outlined
                flat
                dense
                placeholder="Type a message..."
                class="col q-mr-sm shadow-1"
                @keyup.enter="sendMessage"
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
import { onMounted, ref } from 'vue';
import DotsLoader from './DotsLoader.vue';
import { useConversationTurnsStore } from 'src/stores/store-conversation-turns';

const VITE_API_BASE_URL = import.meta.env.VITE_API_BASE_URL as string;
const chat_api_url = `${VITE_API_BASE_URL}/chat`;

const conversation_turns_store = useConversationTurnsStore();

const input_message = ref<string>('');

async function sendMessage() {
    const input = input_message.value;
    if (!input) {
        return;
    }
    input_message.value = '';

    const next_turn_index = conversation_turns_store.addInputTurn(input);
    const body = JSON.stringify({
        msg: input
    })

    console.log('sending chat message', { body, chat_api_url })

    // define an abort controller to override the default fetch timeout
    const abortController = new AbortController();
    const response = await fetch(chat_api_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body,
        signal: abortController.signal
    })
    const reader = response.body?.getReader();
    if (reader) {
        const decoder = new TextDecoder();

        while (true) {
            const { done, value } = await reader.read();
            if (done) {
                break;
            }
            if (value) {
                const fragment: string = decoder.decode(value);
                conversation_turns_store.appendReplyFragmentToTurn(fragment, next_turn_index);
            }
        }
    } else {
        console.error('failed to get chat response reader', { response })
    }
}

onMounted(async () => {
    if (!conversation_turns_store.getTurns.length) {
        input_message.value = 'hello!';
        await sendMessage();
    }
})

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
