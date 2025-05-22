vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

vim.keymap.set('n', '<leader>rp', ':w | !python3 %<CR>', { noremap = true, silent = true, desc = "Save & Run Python File" })
