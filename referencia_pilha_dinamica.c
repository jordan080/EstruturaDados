#include <stdio.h>
#include <malloc.h>

typedef int bool;

typedef struct{
  int id, case_in_country, age;
  bool If_onset_approximated, visiting_Wuhan, from_Wuhan, death, recovered, symptom;
  char reporting_date[15], summary[255], location[255], country[255], gender[20], symptom_onset[15], hosp_visit_date[15], exposure_start[15], exposure_end[15], source[255], link[255];
}CovidLine;

typedef struct Elemento{
  CovidLine reg;
  struct Elemento* next;
}Elemento;

typedef struct{
  Elemento* head;
}ListaLine;

void inicializarLista(ListaLine* l){
  l->head = (Elemento*) malloc(sizeof(Elemento));
  l->head->next = l->head;
}

Elemento* buscar(ListaLine* l, int ch, Elemento** prev){
  *prev = l->head;
  Elemento* aux = l->head->next;
  while(aux->reg.id < ch){
    *prev = aux;
    aux = aux->next;
  }
  if(aux != l->head && aux->reg.id == ch)
    return aux;
  return NULL;
}

bool inserir(ListaLine* l, CovidLine reg){
  Elemento* prev;
  Elemento* aux = buscar(l, reg.id, &prev);
  if(aux != NULL){//mesma chave encontrada, não substitui
    return 0;
  }
  aux = (Elemento*) malloc(sizeof(Elemento));
  aux->reg = reg;
  aux->next = prev->next;
  prev->next = aux;
  return 1;
}

bool exclui(ListaLine* l, int ch){
  Elemento* prev;
  Elemento* aux = buscar(l, ch, &prev);
  if(aux == NULL)
    return 0;
  prev->next = aux->next;
  free(aux);
  return 1;
}

bool modif(ListaLine* l, CovidLine reg){
  Elemento* prev;
  Elemento* aux = buscar(l, reg.id, &prev);
  if(aux == NULL){//não existe elemento
    return 0;
  }
  aux->reg = reg;
  return 1;
}

int main(void) {
  printf("Hello World\n");
  return 0;
}
