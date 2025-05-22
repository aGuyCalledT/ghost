-- ~/.config/nvim/lua/cmp.lua

local cmp = require('cmp')
local luasnip = require('luasnip') -- Nur, wenn Sie LuaSnip verwenden

cmp.setup({
    snippet = {
        -- Optional: Wenn Sie Snippets mit LuaSnip verwenden möchten
        expand = function(args)
            luasnip.lsp_expand(args.body) -- Für Luasnip
        end,
    },
    mapping = cmp.mapping.preset.insert({
        ['<C-b>'] = cmp.mapping.scroll_docs(-4),
        ['<C-f>'] = cmp.mapping.scroll_docs(4),
        ['<C-Space>'] = cmp.mapping.complete(), -- Manuelle Vervollständigung triggern
        ['<C-e>'] = cmp.mapping.abort(),
        ['<CR>'] = cmp.mapping.confirm({ select = true }), -- Ausgewählten Vorschlag bestätigen
        ['<Tab>'] = cmp.mapping(function(fallback)
            if cmp.visible() then
                cmp.select_next_item() -- Nächstes Element in der Vervollständigungsliste auswählen
            elseif luasnip.expand_or_jumpable() then
                luasnip.expand_or_jumpable() -- Durch Snippets springen (wenn aktiv)
            else
                fallback() -- Normales Tab-Verhalten
            end
        end, { 'i', 's' }),
        ['<S-Tab>'] = cmp.mapping(function(fallback)
            if cmp.visible() then
                cmp.select_prev_item() -- Vorheriges Element in der Vervollständigungsliste auswählen
            elseif luasnip.jumpable(-1) then
                luasnip.jumpable(-1) -- Durch Snippets springen (wenn aktiv)
            else
                fallback()
            end
        end, { 'i', 's' }),
    }),
    sources = cmp.config.sources({
        { name = 'nvim_lsp' },    -- LSP-Vorschläge (von Pyright)
        { name = 'luasnip' },     -- Snippet-Vorschläge
        { name = 'buffer' },      -- Wörter aus dem aktuellen Buffer
        { name = 'path' },        -- Dateipfade
    }),
    -- Optional: Symbole für die verschiedenen Vorschlagstypen (Funktion, Variable etc.)
    formatting = {
        -- format = require('lspkind').cmp_format, -- Wenn Sie lspkind installieren möchten
    },
})

-- Optional: Empfohlene Konfiguration für lspkind.nvim, wenn Sie es installieren
-- use('onsails/lspkind.nvim') -- Fügen Sie dies zu Ihrem Packer-Block hinzu
-- Setzen Sie das 'capabilities'-Feld für lspconfig, damit es mit cmp zusammenarbeitet
-- Dies ist sehr wichtig, damit Pyright die richtigen Informationen an cmp sendet
local capabilities = require('cmp_nvim_lsp').default_capabilities()
require('lspconfig').pyright.setup({
    capabilities = capabilities,
    -- ... Ihre anderen Pyright-Einstellungen ...
})

-- Beispiel für weitere LSP-Server
-- require('lspconfig').lua_ls.setup({
--     capabilities = capabilities,
--     settings = {
--         Lua = {
--             diagnostics = {
--                 globals = { 'vim' }
--             }
--         }
--     }
-- })




