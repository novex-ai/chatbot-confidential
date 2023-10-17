<template>
    <q-table
        title="Knowledge Files"
        :columns="columns"
        :rows="rows"
        row-key="name"
    />
</template>

<script setup>
const columns = [
    {
        name: 'name',
        required: true,
        label: 'Name',
        align: 'left',
        field: 'name',
        sortable: true
    },
    {
        name: 'uploaded',
        align: 'center',
        label: 'Uploaded',
        field: 'uploaded',
        sortable: true
    },
    {
        name: 'size_bytes',
        align: 'right',
        label: 'Size (bytes)',
        field: 'size_bytes',
        format: (val) => val.toFixed(2),
        sortable: true
    },
    {
        name: 'status',
        align: 'center',
        label: 'Status',
        field: 'status',
        sortable: true
    }
];

const rows = [
    {
        name: 'sales_call_transcript_001.txt',
        uploaded: '2023-09-01 12:00:00',
        size_bytes: 123456,
        status: 'PROCESSED'
    },
    {
        name: 'sales_training.txt',
        uploaded: '2023-09-03 12:00:00',
        size_bytes: 500000,
        status: 'PROCESSED'
    }
];
</script>
