-- Bootstrap Packer (Plugin-Manager)
local packer_bootstrap = vim.fn.stdpath('data') .. '/site/pack/packer/start/packer.nvim'
if vim.fn.empty(vim.fn.glob(packer_bootstrap)) > 0 then
    vim.fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', packer_bootstrap})
    vim.cmd('packadd packer.nvim')
end

-- Packer-Konfiguration
require('packer').startup(function(use)
    use 'wbthomason/packer.nvim'
    use 'nvim-telescope/telescope.nvim'
    use 'nvim-lua/plenary.nvim' -- Abhängigkeit für Telescope

    use {"catppuccin/nvim", as = "catppucin"}
    use('nvim-treesitter/nvim-treesitter', {run = ':TSUpdate'})
    use('ThePrimeagen/harpoon')

    -- LSP und Autovervollständigung
    use ('neovim/nvim-lspconfig')
    use 'hrsh7th/nvim-cmp'
    use 'hrsh7th/cmp-nvim-lsp'
    use 'hrsh7th/cmp-buffer'
    use 'hrsh7th/cmp-path'
    use 'saadparwaiz1/cmp_luasnip'
    use 'L3MON4D3/LuaSnip'
    use 'rafamadriz/friendly-snippets'
    -- use 'onsails/lspkind.nvim' -- Für schöne Icons in der Autovervollständigung
end)

-- Globale Neovim-Optionen
vim.opt.clipboard = "unnamedplus"

-- Externe Konfigurationsdateien laden
require("t_module")    -- Ihr persönliches Modul
require('lsp')         -- LSP-Server Konfiguration (inkl. Pyright)
require('cmp_config')  -- nvim-cmp Autovervollständigung Konfiguration
