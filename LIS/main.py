import graphviz
import uuid

def build_labeled_lis_tree(sequence):
    memo = {}
    def get_lis_len_starting_at(idx):
        if idx in memo: return memo[idx]
        current_val = sequence[idx]
        max_sub_len = 0
        for i in range(idx + 1, len(sequence)):
            if sequence[i] > current_val:
                max_sub_len = max(max_sub_len, get_lis_len_starting_at(i))
        memo[idx] = 1 + max_sub_len
        return 1 + max_sub_len

    global_max_lis = 0
    for i in range(len(sequence)):
        global_max_lis = max(global_max_lis, get_lis_len_starting_at(i))

    dot = graphviz.Digraph('LIS_Tree_Final', comment='LIS Tree with Label')
    
    label_text = f"\nVisualisasi LIS Tree\nMaximum LIS Length: {global_max_lis}\n(Jalur Merah)"
    dot.attr(label=label_text, labelloc='t', fontsize='20', fontname='Arial Bold')
    
    dot.attr(rankdir='TB', splines='line')
    dot.attr('node', shape='circle', style='filled', fillcolor='white', fontname='Arial')

    root_id = str(uuid.uuid4())
    dot.node(root_id, '', width='0.3')

    def add_nodes(parent_id, current_idx, needed_len, is_on_path):
        current_val = sequence[current_idx]
        
        color = 'red' if is_on_path else 'black'
        penwidth = '2.0' if is_on_path else '1.0'
        
        node_id = str(uuid.uuid4())
        
        dot.node(node_id, str(current_val), color=color, fontcolor=color, penwidth=penwidth)
        dot.edge(parent_id, node_id, color=color, penwidth=penwidth)
        
        for next_idx in range(current_idx + 1, len(sequence)):
            if sequence[next_idx] > current_val:
                child_lis_len = get_lis_len_starting_at(next_idx)
                is_child_optimal = is_on_path and (child_lis_len == needed_len - 1)
                
                add_nodes(node_id, next_idx, child_lis_len, is_child_optimal)

    for i in range(len(sequence)):
        lis_len_from_here = get_lis_len_starting_at(i)
        
        is_start_optimal = (lis_len_from_here == global_max_lis)
        
        add_nodes(root_id, i, lis_len_from_here, is_start_optimal)

    return dot

# soal : 4, 1, 13, 7, 0, 2, 8, 11, 3
raw_input = input("Masukkan angka dipisah spasi: ")
data = [int(x) for x in raw_input.split()]

print("Membuat grafik dengan label...")
final_tree = build_labeled_lis_tree(data)
final_tree.render('lis_tree_final_labeled', format='png', cleanup=True, view=True)
print("Selesai! Cek gambar 'lis_tree_final_labeled.png'")