from collections import MutableMapping

class MapBase(MutableMapping):
    class Item(object):
        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __eq__(self, other):
            return self.key == other.key

        def __nq__(self, other):
            return self.key != other.key

        def __lt__(self, other):
            return self.key < other.key

        def __gt__(self, other):
            return self.key > other.key

class UnsortedTableMap(MapBase):
    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def __getitem__(self, k):
        for item in self.table:
            if k == item.key:
                return item.value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        for item in self.table:
            if k == item.key:
                item.value = v
                return
        self.table.append(self.Item(k, v))

    def __delitem__(self, k):
        for j in range(len(self)):
            if k == self.table[j].key:
                self.table.pop()
                return
        raise KeyError('Key Error: ' + repr(k))

    def __iter__(self):
        for item in self.table:
            yield item.key

class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self.table = [None for i in range(cap)]
        self.n = 0
        self.prime = p
        self.scale = 1 + randrange(p - 1)
        self.shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k) * self.scale + self.shift) \
                    % self.prime \
                    % self.len(self.table)

    def _bucket_getitem(self, j, k):
        raise NotImplementedError('in _bucket_getitem')

    def _bucket_setitem(self, j, k, v):
        raise NotImplementedError('in _bucket_setitem')

    def _bucket_delitem(self, j, k):
        raise NotImplementedError('in _bucket_delitem')

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self.n > len(self.table) // 2:
            self._resize(len(2 * len(self.table) - 1))

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self.n -= 1

    def _resize(self, c):
        old = list(self.items())
        self.table = [None for i in range(c)]
        self.n = 0
        for (k, v) in old:
            self[k] = v

class ChainHashMap(HashMapBase):
    def _bucket_getitem(self, j, k):
        bucket = self.table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self.table[j] is None:
            self.table[j] = UnsortedTableMap()
        oldsize = len(self.table[j])
        self.table[j][k] = v
        if len(self.table[j]) > oldsize:
            self.n += 1

    def _bucket_delitem(self, j, k):
        bucket = self.table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self.table:
            if bucket is not None:
                for key in bucket:
                    yield key

class ProbeHashMap(HashMapBase):
    _AVAIL = object()

    def _is_available(self, j):
        return self.table[j] is None \
                or self.table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self.table[j] is None:
                    return (False, firstAvail)
            elif k == self.table[j].key:
                return (True, j)
            j = (j + 1) % len(self.table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self.table[s].value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self.table[s] = self.Item(k, v))
            self.n += 1
        else:
            self.table[s].value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self.table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self.table)):
            if not self._is_available(j):
                yield self.table[j].key

class SortedTableMap(MapBase):
    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self.table[mid].key:
                return mid
            elif k < self.table[mid].key:
                self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j == len(self.table) or self.table[j].key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self.table[j].value

    def __setitem__(self, k, v):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table) and self.table[j].key == k:
            self.table[j].value = v
        else:
            self.table.insert(j, self.Item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j == len(self.table) or self.table[j].key != k:
            raise KeyError('Key Error: ' + repr(k))
        self.table.pop(j)

    def __iter__(self):
        for item in self.table:
            yield item.key

    def __reversed__(self):
        for item in reversed(self.table):
            yield item.key

    def find_min(self):
        if len(self.table) > 0:
            return (self.table[0].key, self.table[0].value)
        else:
            return None

    def find_max(self):
        if len(self.table) > 0:
            return (self.table[-1].key, self.table[-1].value)
        else:
            return None

    def find_ge(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table):
            return (self.table[j].key, self.table[j].value)
        else:
            return None

    def find_lt(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j > 0:
            return (self.table[j - 1].key, self.table[j - 1].value)
        else:
            return None

    def find_gt(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table) and self.table.key == k:
            j += 1
        if j < len(self.table):
            return (self.table[j].key, self.table[j].value)
        else:
            return None

    def find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self.table) - 1)
        while j < len(self.table) and (stop is None or self.table[j].key < stop):
            yield (self.table[j].key, self.table[j].value)
            j += 1
