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
import { inject, ref, reactive } from 'vue';
import { AxiosInstance } from 'axios';
import { DateTime } from 'luxon';
import DotsLoader from './DotsLoader.vue';


const $api = inject('$api') as AxiosInstance;

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
        input_datetime: DateTime.now(),
        reply: ''
    })
    input_message.value = '';

    const response = await $api({
        method: 'post',
        url: '/chat',
        data: {
            msg: input
        },
        responseType: 'stream'
    })
    conversation_turns[next_turn_index].reply += response.data;
    conversation_turns[next_turn_index].reply_datetime = DateTime.now();
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
